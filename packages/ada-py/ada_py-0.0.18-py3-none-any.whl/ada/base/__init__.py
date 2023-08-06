import logging
import os
import pathlib

from ada.config import Settings as _Settings
from ada.core.constants import color_map as _cmap
from ada.visualize.renderer import MyRenderer


class Backend:
    def __init__(self, name, guid=None, metadata=None, units="m", parent=None, ifc_settings=None, ifc_elem=None):
        self.name = name
        self.parent = parent
        self._ifc_settings = ifc_settings
        from ada.ifc.utils import create_guid

        self.guid = create_guid() if guid is None else guid
        units = units.lower()
        if units not in _Settings.valid_units:
            raise ValueError(f'Unit type "{units}"')
        self._units = units
        self._metadata = metadata if metadata is not None else dict(props=dict())
        self._ifc_elem = ifc_elem
        # TODO: Currently not able to keep and edit imported ifc_elem objects
        self._ifc_elem = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if _Settings.convert_bad_names:
            logging.debug("Converting bad name")
            value = value.replace("/", "_").replace("=", "")
            if str.isnumeric(value[0]):
                value = "ADA_" + value

        if "/" in value:
            logging.debug(f'Character "/" found in {value}')

        self._name = value.strip()

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):
        if value is None:
            raise ValueError("guid cannot be None")
        self._guid = value

    @property
    def parent(self):
        """

        :return:
        :rtype: ada.Part
        """
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def metadata(self):
        return self._metadata

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, value):
        raise NotImplementedError("Assigning units is not yet represented for this object")

    @staticmethod
    def _unit_conversion(ori_unit, value):
        if value == "m" and ori_unit == "mm":
            scale_factor = 0.001
        elif value == "mm" and ori_unit == "m":
            scale_factor = 1000
        else:
            raise ValueError(f'Unrecognized unit conversion from "{ori_unit}" to "{value}"')
        return scale_factor

    @property
    def ifc_settings(self):
        if self._ifc_settings is None:
            import ifcopenshell.geom

            ifc_settings = ifcopenshell.geom.settings()
            ifc_settings.set(ifc_settings.USE_PYTHON_OPENCASCADE, True)
            ifc_settings.set(ifc_settings.SEW_SHELLS, True)
            ifc_settings.set(ifc_settings.WELD_VERTICES, True)
            ifc_settings.set(ifc_settings.INCLUDE_CURVES, True)
            ifc_settings.set(ifc_settings.USE_WORLD_COORDS, True)
            ifc_settings.set(ifc_settings.VALIDATE_QUANTITIES, True)
            self._ifc_settings = ifc_settings
        return self._ifc_settings

    @ifc_settings.setter
    def ifc_settings(self, value):
        self._ifc_settings = value

    @property
    def ifc_elem(self):
        if self._ifc_elem is None:
            self._ifc_elem = self._generate_ifc_elem()
        return self._ifc_elem

    def get_assembly(self):
        """

        :return:
        :rtype: ada.Assembly
        """
        from ada import Assembly

        parent = self
        still_looking = True
        max_levels = 10
        a = 0
        while still_looking is True:
            if issubclass(type(parent), Assembly) is True:
                still_looking = False
            if parent.parent is None:
                break
            a += 1
            parent = parent.parent
            if a > max_levels:
                logging.info(f"Max levels reached. {self} is highest level element")
                break
        return parent

    def _generate_ifc_elem(self):
        raise NotImplementedError("")

    def remove(self):
        """
        Remove this element/part from assembly/part
        """
        from ada import Beam, Part, Shape

        if self.parent is None:
            logging.error(f"Unable to delete {self.name} as it does not have a parent")
            return

        # if self._ifc_elem is not None:
        #     a = self.parent.get_assembly()
        # f = a.ifc_file
        # This returns results in a failure error
        # f.remove(self.ifc_elem)

        if type(self) is Part:
            self.parent.parts.pop(self.name)
        elif issubclass(type(self), Shape):
            self.parent.shapes.pop(self.parent.shapes.index(self))
        elif type(self) is Beam:
            self.parent.beams.remove(self)
        else:
            raise NotImplementedError()


class BackendGeom(Backend):
    """
    The shared backend of all physical components (Beam, Plate) or aggregate of components (Part, Assembly).

    """

    _renderer = None

    def __init__(self, name, guid=None, metadata=None, units="m", parent=None, colour=None, ifc_elem=None):
        super().__init__(name, guid, metadata, units, parent, ifc_elem=ifc_elem)
        self._penetrations = []
        self.colour = colour

    def add_penetration(self, pen):
        from ada import Penetration, PrimBox, PrimCyl, PrimExtrude, PrimRevolve

        if type(pen) not in [Penetration, PrimExtrude, PrimRevolve, PrimCyl, PrimBox]:
            raise ValueError(f'Unsupported penetration type "{type(pen)}"')

        pen.parent = self
        if type(pen) in (PrimExtrude, PrimRevolve, PrimCyl, PrimBox):
            pen = Penetration(pen, parent=self)
            self._penetrations.append(pen)
        else:
            self._penetrations.append(pen)

        return pen

    def to_stp(self, destination_file, geom_repr="solid", schema="AP242"):
        """
        Write current assembly to STEP file

        OpenCascade reference:

            https://www.opencascade.com/doc/occt-7.4.0/overview/html/occt_user_guides__step.html#occt_step_3


        :param destination_file:
        :param geom_repr:
        :param schema: STEP Schemas.
        """

        from OCC.Core.IFSelect import IFSelect_RetError
        from OCC.Core.Interface import Interface_Static_SetCVal
        from OCC.Core.STEPConstruct import stepconstruct_FindEntity
        from OCC.Core.STEPControl import STEPControl_AsIs, STEPControl_Writer
        from OCC.Core.TCollection import TCollection_HAsciiString

        from ada.core.utils import Counter

        if geom_repr not in ["shell", "solid"]:
            raise ValueError('Geometry representation can only accept either "solid" or "shell" as input')

        destination_file = pathlib.Path(destination_file).with_suffix(".stp")

        assembly_mode = 1
        shp_names = Counter(1, "shp")
        writer = STEPControl_Writer()
        fp = writer.WS().TransferWriter().FinderProcess()
        Interface_Static_SetCVal("write.step.schema", schema)
        # Interface_Static_SetCVal('write.precision.val', '1e-5')
        Interface_Static_SetCVal("write.precision.mode", "1")
        Interface_Static_SetCVal("write.step.assembly", str(assembly_mode))

        from ada import Assembly, Beam, Part, Pipe, Plate, Shape, Wall

        def add_geom(geo, o):
            name = o.name if o.name is not None else next(shp_names)
            Interface_Static_SetCVal("write.step.product.name", name)
            stat = writer.Transfer(geo, STEPControl_AsIs)
            if int(stat) > int(IFSelect_RetError):
                raise Exception("Some Error occurred")

            item = stepconstruct_FindEntity(fp, geo)
            if not item:
                logging.debug("STEP item not found for FindEntity")
            else:
                item.SetName(TCollection_HAsciiString(name))

        if type(self) is Shape:
            assert isinstance(self, Shape)
            add_geom(self.geom, self)
        elif type(self) in (Beam, Plate, Wall):
            assert isinstance(self, (Beam, Plate, Wall))
            if geom_repr == "shell":
                add_geom(self.shell, self)
            else:
                add_geom(self.solid, self)
        elif type(self) is Pipe:
            assert isinstance(self, Pipe)
            for geom in self.geometries:
                add_geom(geom, self)
        elif type(self) in (Part, Assembly):
            assert isinstance(self, Part)

            for p in self.get_all_subparts() + [self]:
                for obj in list(p.plates) + list(p.beams) + list(p.shapes) + list(p.pipes) + list(p.walls):
                    if type(obj) in (Plate, Beam, Wall):
                        try:
                            if geom_repr == "shell":
                                add_geom(obj.shell, self)
                            else:
                                add_geom(obj.solid, self)
                        except BaseException as e:
                            logging.info(f'passing pl "{obj.name}" due to {e}')
                            continue
                    elif type(obj) in (Pipe,):
                        assert isinstance(obj, Pipe)
                        for geom in obj.geometries:
                            add_geom(geom, self)
                    elif type(obj) is Shape:
                        add_geom(obj.geom, self)
                    else:
                        raise ValueError("Unkown Geometry type")

        os.makedirs(destination_file.parent, exist_ok=True)

        status = writer.Write(str(destination_file))
        if int(status) > int(IFSelect_RetError):
            raise Exception("Error during write operation")

        print(f'step file created at "{destination_file}"')

    def render_locally(
        self, addr="localhost", server_port=8080, open_webbrowser=False, render_engine="threejs", resolution=(1800, 900)
    ):
        from OCC.Display.WebGl.simple_server import start_server

        if render_engine == "xdom":
            from OCC.Display.WebGl import x3dom_renderer

            my_renderer = x3dom_renderer.X3DomRenderer()
            # TODO: Find similarities in build processing as done for THREE.js (tesselate geom etc..).
            # my_renderer.DisplayShape(shape.profile_curve_outer.wire)
            # my_renderer.DisplayShape(shape.sweep_curve.wire)
            # my_renderer.DisplayShape(shape.geom)
            my_renderer.render()
        else:  # Assume THREEJS
            from ipywidgets.embed import embed_minimal_html

            _path = pathlib.Path("temp/index.html").resolve().absolute()

            renderer = MyRenderer(resolution)
            renderer.DisplayObj(self)
            renderer.build_display()

            os.makedirs(_path.parent, exist_ok=True)
            embed_minimal_html(_path, views=renderer._renderer, title="Pythreejs Viewer")
            start_server(addr, server_port, str(_path.parent), open_webbrowser)

    def get_render_snippet(self, view_size=None):
        """
        Return the html snippet containing threejs renderer
        """
        from ipywidgets.embed import embed_snippet

        renderer = MyRenderer()
        renderer.DisplayObj(self)
        renderer.build_display()

        return embed_snippet(renderer._renderer)

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        if type(value) is str:
            if value.lower() not in _cmap.keys():
                raise ValueError("Currently unsupported")
            self._colour = _cmap[value.lower()]
        else:
            self._colour = value

    @property
    def colour_webgl(self):
        from OCC.Display.WebGl.jupyter_renderer import format_color

        if self.colour is None:
            return None
        if self.colour[0] == -1 and self.colour[1] == -1 and self.colour[2] == -1:
            return None

        if self.colour[0] <= 1.0:
            colour = [int(x * 255) for x in self.colour]
        else:
            colour = [int(x) for x in self.colour]

        colour_formatted = format_color(*colour)
        return colour_formatted

    @property
    def penetrations(self):
        return self._penetrations

    def _repr_html_(self):
        from IPython.display import display
        from ipywidgets import HBox, VBox

        renderer = MyRenderer()

        renderer.DisplayObj(self)
        renderer.build_display()
        self._renderer = renderer
        display(HBox([VBox([HBox(renderer._controls), renderer._renderer]), renderer.html]))
        # renderer._reset()
        # self._renderer.Display()
        return ""

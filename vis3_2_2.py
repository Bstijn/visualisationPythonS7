from vtkmodules.all import (
    vtkStructuredGridReader, vtkDataSetMapper,
    vtkLookupTable, vtkProperty,
    vtkActor,vtkGlyph3D, vtkArrowSource

)
from util.window_renderer import WindowRenderer

class Isoline:
    def __init__(self, renderer):
        self.__renderer = renderer
        self.__reader = vtkStructuredGridReader()
        self.__mapper = vtkDataSetMapper()
        self.__lookup_table = vtkLookupTable()
        self.__property = vtkProperty()
        self.__actor = vtkActor()
        self.__glyph = vtkGlyph3D()
        self.__arrow = vtkArrowSource()

    def setup(self, filename, scale):
        # setup reader
        self.__reader.SetFileName(filename)
        self.__reader.Update()

        # lookuptable pretty much same as 3-1-1
        self.__setup_lookup_table()
        self.setupArrow()
        self.setupGlyph()

        self.__mapper.SetInputConnection(self.__glyph.GetOutputPort())
        self.__mapper.SetLookupTable(self.__lookup_table)
        self.__mapper.SetScalarRange(0.0,1.0)
        self.__mapper.ScalarVisibilityOn()
        self.__mapper.Update()


        self.__actor.SetMapper(self.__mapper)
        self.__renderer.AddActor(self.__actor)

    def __setup_lookup_table(self):
        self.__lookup_table.SetNumberOfColors(1000)
        self.__lookup_table.SetHueRange(0.0, 1.0)
        self.__lookup_table.SetSaturationRange(1.0, 0.0)
        self.__lookup_table.SetValueRange(1.0, 0.0)
        self.__lookup_table.SetAlphaRange(1.0, 0.0)

        # Range of scalars that will be mapped
        self.__lookup_table.SetRange(0.0, 1.0)
        self.__lookup_table.Build()

    def setupArrow(self):
        self.__arrow.SetTipLength(0.25)
        self.__arrow.SetTipRadius(0.1)
        self.__arrow.SetTipResolution(10)

    def setupGlyph(self):
        self.__glyph = vtkGlyph3D()
        self.__glyph.SetSourceConnection(self.__arrow.GetOutputPort())
        self.__glyph.SetInputConnection(self.__reader.GetOutputPort())
        self.__glyph.SetVectorModeToUseVector()
        self.__glyph.SetColorModeToColorByScalar()
        self.__glyph.SetScaleModeToDataScalingOff()
        self.__glyph.OrientOn()
        self.__glyph.SetScaleFactor(0.2)

if __name__ == "__main__":
    renderer = WindowRenderer()
    Isoline(renderer.renderer).setup("vtkfiles/density.vtk",0.01)

    renderer.setup_render_window()
    renderer.start_render_window()
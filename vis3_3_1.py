from vtkmodules.all import (
    vtkStructuredGridReader, vtkDataSetMapper,
    vtkLookupTable, vtkProperty,
    vtkActor,
    vtkPolyData,
    vtkPlane,
    vtkCutter
)
from util.window_renderer import WindowRenderer

class cutter:
    def __init__(self, renderer):
        self.__renderer = renderer
        self.__reader = vtkStructuredGridReader()
        self.__mapper = vtkDataSetMapper()
        self.__lookup_table = vtkLookupTable()
        self.__property = vtkProperty()
        self.__actor = vtkActor()

    def setup(self, filename):
        # setup reader
        self.__reader.SetFileName(filename)
        self.__reader.Update()

        # lookuptable pretty much same as 3-1-1
        self.__setup_lookup_table()
        self.__setup_cutter()
        self.__mapper.SetInputConnection(self.__cutter.GetOutputPort())
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

    def __setup_cutter(self):
        self.__plane = vtkPlane()
        self.__plane.SetOrigin(self.__reader.GetOutput().GetCenter())
        self.__plane.SetNormal(0,0,1.0)
        self.__cutter = vtkCutter()
        self.__cutter.SetInputConnection(self.__reader.GetOutputPort())
        self.__cutter.SetCutFunction(self.__plane)
        self.__cutter.Update()


if __name__ == "__main__":
    renderer = WindowRenderer()
    cutter(renderer.renderer).setup("vtkfiles/density.vtk")

    renderer.setup_render_window()
    renderer.start_render_window()
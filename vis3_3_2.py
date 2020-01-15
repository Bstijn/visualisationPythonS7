from vtkmodules.all import (
    vtkStructuredGridReader, vtkDataSetMapper,
    vtkLookupTable, vtkProperty,
    vtkActor,
    vtkPolyData,
    vtkSphere,
    vtkClipDataSet
)
from util.window_renderer import WindowRenderer

class clipper:
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
        self.__setup_clipper()
        self.__mapper.SetInputConnection(self.__clipper.GetOutputPort())
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

    def __setup_clipper(self):
        self.__sphere = vtkSphere()
        self.__sphere.SetCenter(self.__reader.GetOutput().GetCenter())
        self.__sphere.SetRadius(5.3)
        self.__clipper = vtkClipDataSet()
        self.__clipper.SetInputConnection(self.__reader.GetOutputPort())
        self.__clipper.SetClipFunction(self.__sphere)
        self.__clipper.Update()


if __name__ == "__main__":
    renderer = WindowRenderer()
    clipper(renderer.renderer).setup("vtkfiles/density.vtk")

    renderer.setup_render_window()
    renderer.start_render_window()
from vtkmodules.all import (
    vtkStructuredGridReader, vtkDataSetMapper,
    vtkLookupTable, vtkProperty,
    vtkActor, vtkPointSource, vtkLineSource, vtkRungeKutta4, vtkStreamTracer

)
from util.window_renderer import WindowRenderer

class streamline:
    def __init__(self, renderer):
        self.__renderer = renderer
        self.__reader = vtkStructuredGridReader()
        self.__mapper = vtkDataSetMapper()
        self.__lookup_table = vtkLookupTable()
        self.__property = vtkProperty()
        self.__actor = vtkActor()
        self.__points = vtkPointSource()
        self.__rungeKutta = vtkRungeKutta4()
        self.__streamer = vtkStreamTracer()

    def setup(self, filename):
        # setup reader
        self.__reader.SetFileName(filename)
        self.__reader.Update()

        # lookuptable pretty much same as 3-1-1
        self.__setup_lookup_table()
        self.setupStreamline()

        self.__mapper.SetInputConnection(self.__streamer.GetOutputPort())
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

    def setupStreamline(self):
        self.__points.SetRadius(3.0)
        self.__points.SetCenter((self.__reader.GetOutput()).GetCenter())
        self.__points.SetNumberOfPoints(100)

        self.__streamer.SetInputConnection(self.__reader.GetOutputPort())
        self.__streamer.SetSourceConnection(self.__points.GetOutputPort())
        self.__streamer.SetMaximumPropagation(100)
        self.__streamer.SetInitialIntegrationStep(0.1)
        self.__streamer.SetIntegrationDirectionToBoth()
        self.__streamer.SetIntegrator(self.__rungeKutta)
        self.__streamer.Update()


if __name__ == "__main__":
    renderer = WindowRenderer()
    streamline(renderer.renderer).setup("vtkfiles/density.vtk")

    renderer.setup_render_window()
    renderer.start_render_window()
from vtkmodules.all import (
    vtkStructuredGridReader,vtkPolyDataMapper,
    vtkProperty,
    vtkActor, vtkContourFilter
)

from util.window_renderer import WindowRenderer

class ContourVisualizer:
    def __init__(self, renderer):
        self.__renderer = renderer
        self.__mapper = vtkPolyDataMapper()
        self.__filter = vtkContourFilter()
        self.__reader = vtkStructuredGridReader()
        self.__actor = vtkActor()
        self.__property = vtkProperty()

    def setup(self,file_name):
        # Reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Filter
        self.__filter.SetInputConnection(self.__reader.GetOutputPort())
        self.__filter.SetValue(0,0.26)

        # Mapper
        self.__mapper.SetInputConnection(self.__filter.GetOutputPort())

        self.__actor.SetMapper(self.__mapper)

        self.__renderer.AddActor(self.__actor)


if __name__ == "__main__":
    renderer = WindowRenderer()
    ContourVisualizer(renderer.renderer).setup("vtkfiles/subset.vtk")

    renderer.setup_render_window()
    renderer.start_render_window()



from vtkmodules.all import (
    vtkPolyDataReader, vtkProperty,
    vtkPolyDataMapper, vtkActor,
    vtkStructuredPointsReader, vtkGeometryFilter,
)
from util.window_renderer import WindowRenderer
from vis1_3 import Cylinder
from vis1_2 import Text
from vis1 import Cone
from vis2_1 import ObjVisualizer

class VtkVisualizer:
    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkStructuredPointsReader()
        self.__property = vtkProperty()
        self.__geometry_filter = vtkGeometryFilter()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self, file_name):
        """Setup the VTK structured points reader"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set property
        self.__property.SetColor(1.0, 0.0, 0.0)

        self.__geometry_filter.SetInputConnection(self.__reader.GetOutputPort())
        self.__geometry_filter.Update()

        # Set mapper
        self.__mapper.SetInputConnection(self.__geometry_filter.GetOutputPort())
        self.__mapper.Update()

        # Set  actor
        self.__actor.SetProperty(self.__property)
        self.__actor.SetMapper(self.__mapper)

        # Add actor to the window renderer
        self.__renderer.AddActor(self.__actor)

if __name__ == '__main__':
    window_renderer = WindowRenderer()
    VtkVisualizer(window_renderer.renderer).setup("vtkfiles/brain.vtk")
    #setup and start window
    window_renderer.setup_render_window()
    window_renderer.start_render_window()
from vtkmodules.all import (
    vtkPolyDataReader, vtkPolyDataMapper, vtkActor
)
from util.window_renderer import WindowRenderer
from vis1_3 import Cylinder
from vis1_2 import Text
from vis1 import Cone
from vis2_1 import ObjVisualizer

class VtkVisualizer:
    def __init__(self, windowrenderer):
        self.__renderer = windowrenderer
        self.__vtk_reader = vtkPolyDataReader()
        self.__actor = vtkActor()
        self.__data_mapper = vtkPolyDataMapper()

    def setup_object(self,filepath):
        #get file
        self.__vtk_reader.SetFileName(filepath)
        # setup mapper and actor
        self.__data_mapper.SetInputConnection(self.__vtk_reader.GetOutputPort())
        self.__actor.SetMapper(self.__data_mapper)
        # renderer
        self.__renderer.AddActor(self.__actor)

if __name__ == '__main__':
    window_renderer = WindowRenderer()
    VtkVisualizer(window_renderer.renderer).setup_object("vtkfiles/brain.vtk")
    #setup and start window
    window_renderer.setup_render_window()
    window_renderer.start_render_window()
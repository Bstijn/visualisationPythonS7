from vtkmodules.all import (
    vtkOBJReader, vtkPolyDataMapper, vtkActor
)
from util.window_renderer import WindowRenderer
from vis1_3 import Cylinder
from vis1_2 import Text
from vis1 import Cone

class ObjVisualizer:
    def __init__(self, renderer):
        self.__renderer = renderer
        self.__vtkOBJReader = vtkOBJReader()
        self.__objMapper = vtkPolyDataMapper()
        self.__objActor = vtkActor()

    def setup_object(self, file_path):
        # Get file
        self.__vtkOBJReader.SetFileName(file_path)
        #setup mapper and actor
        self.__objMapper.SetInputConnection(self.__vtkOBJReader.GetOutputPort())
        self.__objActor.SetMapper(self.__objMapper)
        #renderer
        self.__renderer.AddActor(self.__objActor)

# run
if __name__ == '__main__':
    windowrenderer = WindowRenderer()
    ObjVisualizer(windowrenderer.renderer).setup_object("objfiles/doggo.obj")
    Text(windowrenderer.renderer).setup_text("  this is a dog")
    windowrenderer.setup_render_window()
    windowrenderer.start_render_window()
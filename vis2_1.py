from vtkmodules.all import (
    vtkOBJReader, vtkPolyDataMapper, vtkActor
)
from util.window_renderer import WindowRenderer


class ObjVisualizer:
    def __init__(self, renderer):
        self.__renderer = renderer
        self.__vtkOBJReader = vtkOBJReader()
        self.__objMapper = vtkPolyDataMapper()
        self.__objActor = vtkActor()

    def setupObject(self, file_path):
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
    ObjVisualizer(windowrenderer.renderer).setupObject("objfiles/doggo.obj")

    windowrenderer.setup_render_window()
    windowrenderer.start_render_window()
from vtkmodules.all import (
    vtkPlaneSource, vtkBMPReader,
    vtkTexture, vtkPolyDataMapper,
    vtkActor,
)

from util.window_renderer import WindowRenderer

class VtkTextureReader:
    def __init__(self, windowrenderer):
        #Renderer
        self.__renderer = windowrenderer

        #vtk import variables
        self.__plane = vtkPlaneSource()
        self.__reader = vtkBMPReader()
        self.__texture = vtkTexture()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()

    def setup(self,file_name):
        # Reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()
        #Texture
        self.__texture.SetInputConnection(self.__reader.GetOutputPort())

        # Mapper
        self.__mapper.SetInputConnection(self.__plane.GetOutputPort())

        # Actor
        self.__actor.SetTexture(self.__texture)
        self.__actor.SetMapper(self.__mapper)

        # Renderer
        self.__renderer.AddActor(self.__actor)


if __name__ == '__main__':
    windowrenderer = WindowRenderer()
    VtkTextureReader(windowrenderer.renderer).setup("images/stuff.bmp")

    windowrenderer.setup_render_window()
    windowrenderer.start_render_window()
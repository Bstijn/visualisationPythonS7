from vtkmodules.all import (
    vtkConeSource, vtkPolyDataMapper, vtkActor, vtkTextSource, vtkTextMapper
)

from util.window_renderer import WindowRenderer

class Text:

    def __init__(self, renderer):
        self.__renderer = renderer
        self.__text = vtkTextSource()
        self.__poly_mapper = vtkPolyDataMapper()
        self.__vtkactor = vtkActor()

    def setup_text(self, text):
        #set text
        self.__text.SetText(text)
        self.__text.SetForegroundColor(1,0,0)
        self.__poly_mapper.SetInputConnection(self.__text.GetOutputPort())
        self.__vtkactor.SetMapper(self.__poly_mapper)
        self.__renderer.AddActor(self.__vtkactor)


if __name__ == '__main__':
    window_renderer = WindowRenderer()
    Text(window_renderer.renderer).setup_text("HelloWorld")

    window_renderer.setup_render_window()
    window_renderer.start_render_window()
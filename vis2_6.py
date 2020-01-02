from vtkmodules.all import (
    vtkPolyDataReader, vtkProperty,
    vtkPolyDataMapper, vtkActor,vtkGeometryFilter
)
from util.window_renderer import WindowRenderer
from vis1_2 import Text

class VtkVisualiserWithColorAndPosition:
    def __init__(self, renderer):
        self.__renderer = renderer
        self.__reader = vtkPolyDataReader()
        self.__mapper = vtkPolyDataMapper()
        self.__actor = vtkActor()
        self.__property = vtkProperty()
        self.__geometry_filter = vtkGeometryFilter()

    def setup(self, file_name, colorr,colorg,colorb):
        """Setup the VTK structured points reader"""

        # Set reader
        self.__reader.SetFileName(file_name)
        self.__reader.Update()

        # Set property
        self.__property.SetColor(colorr,colorg,colorb)

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
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/brain.vtk",1,1,1)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/blood.vtk",1,0,0)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/brainbin.vtk",0,0,0)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/duodenum.vtk",1,0.25,0.25)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/eye_retna.vtk",1,0.5,0)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/eye_white.vtk",1,1,1)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/heart.vtk",1,0,0)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/ileum.vtk",1,0.25,0.25)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/kidney.vtk",0.5,0.25,0)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/l_intestine.vtk",0.5,0.25,0)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/liver.vtk",0.5,0.25,0)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/lung.vtk",1,0.7,0.7)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/nerve.vtk",0,1,0)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/skeleton.vtk",0.4,0.4,0.4)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/spleen.vtk",1,1,1)
    VtkVisualiserWithColorAndPosition(window_renderer.renderer).setup("util/frog/stomach.vtk",0,0,1)
    # setup and start window
    window_renderer.setup_render_window()
    window_renderer.start_render_window()
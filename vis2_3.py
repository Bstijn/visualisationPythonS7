from vtkmodules.all import (
    vtkUnstructuredGridReader, vtkDataSetMapper,
    vtkProperty, vtkActor,
)

from util.window_renderer import WindowRenderer

class UGVisualiser:
    def __init__(self, renderer):
        """"init setting up variables"""
        self.__renderer = renderer
        self.__gridReader = vtkUnstructuredGridReader()
        self.__mapper = vtkDataSetMapper()
        self.__property = vtkProperty()
        self.__actor = vtkActor()

    def setup(self, filename):
        # setup reader
        self.__gridReader.SetFileName(filename)
        self.__gridReader.Update()

        # get output
        output = self.__gridReader.GetOutput()
        scalar_range = output.GetScalarRange()

        # mapper set
        self.__mapper.SetInputData(self.__gridReader.GetOutput())

        # Property set
        self.__property.EdgeVisibilityOn()
        self.__property.SetLineWidth(2.0)

        # actor setup
        self.__actor.SetMapper(self.__mapper)
        self.__actor.SetProperty(self.__property)

        #add to renderer
        self.__renderer.AddActor(self.__actor)

if __name__ == "__main__":
    renderer = WindowRenderer()
    UGVisualiser(renderer.renderer).setup("vtkfiles/density.vtk")

    renderer.setup_render_window()
    renderer.start_render_window()

from vtkmodules.all import (
    vtkLookupTable, vtkProperty,
    vtkActor, vtkQuadric, vtkExtractVOI,vtkContourFilter, vtkPolyDataMapper,vtkSampleFunction

)
from util.window_renderer import WindowRenderer

class VOI:
    def __init__(self, renderer):
        self.__renderer = renderer
        self.__mapper = vtkPolyDataMapper()
        self.__lookup_table = vtkLookupTable()
        self.__property = vtkProperty()
        self.__actor = vtkActor()

    def setup(self):

        self.__setup_VOI()

        # lookuptable pretty much same as 3-1-1

        self.__mapper.SetInputConnection(self.__contour_filter.GetOutputPort())

        self.__mapper.SetScalarRange(0.0,1.0)
        self.__mapper.ScalarVisibilityOn()
        self.__mapper.Update()


        self.__actor.SetMapper(self.__mapper)
        self.__renderer.AddActor(self.__actor)



    def __setup_VOI(self):
        # initialize
        self.__quadric = vtkQuadric()
        self.__contour_filter = vtkContourFilter()
        self.__sample = vtkSampleFunction()
        self.__extract = vtkExtractVOI()

        self.__quadric.SetCoefficients(.5,1,.2,0,.1,0,0,.2,0,0)
        self.__sample.SetSampleDimensions(30, 30, 30)
        self.__sample.SetImplicitFunction(self.__quadric)
        self.__sample.ComputeNormalsOff()
        self.__extract.SetInputConnection(self.__sample.GetOutputPort())
        self.__extract.SetVOI(0, 29, 0, 29, 15, 15)
        self.__extract.SetSampleRate(1, 2, 3)

        self.__contour_filter.SetInputConnection(self.__extract.GetOutputPort())
        self.__contour_filter.GenerateValues(13, 0.0, 1.2)







if __name__ == "__main__":
    renderer = WindowRenderer()
    VOI(renderer.renderer).setup()

    renderer.setup_render_window()
    renderer.start_render_window()
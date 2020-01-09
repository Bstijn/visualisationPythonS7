from vtkmodules.all import (
    vtkStructuredGridReader, vtkDataSetMapper,
    vtkLookupTable, vtkProperty,
    vtkActor, vtkGeometryFilter
)

from util.window_renderer import WindowRenderer
from vis1_3 import Cone

class SGVisualiser:
    def __init__(self, renderer):
        # Renderer variable is needed to add the actor
        self.__renderer = renderer

        self.__reader = vtkStructuredGridReader()
        self.__mapper = vtkDataSetMapper()
        self.__lookup_table = vtkLookupTable()
        self.__property = vtkProperty()
        self.__actor = vtkActor()

    def setup(self,filename, range):
        # setup reader
        self.__reader.SetFileName(filename)
        self.__reader.Update()



        # set lookuptable
        self.__setup_lookup_table(5000, (0,25))


        # mapper
        self.__mapper.SetInputConnection(self.__reader.GetOutputPort())
        self.__mapper.SetLookupTable(self.__lookup_table)
        self.__mapper.SetScalarRange(range)
        self.__mapper.ScalarVisibilityOn()
        self.__mapper.Update()

        # Actor
        self.__actor.SetMapper(self.__mapper)
        # propertys
        self.__property = self.__actor.GetProperty()
        self.__actor.SetProperty(self.__property)

        # windowrenderer
        self.__renderer.AddActor(self.__actor)


    def __setup_lookup_table(self, number_of_colors, hue_range):
        self.__lookup_table.SetNumberOfColors(number_of_colors)
        self.__lookup_table.SetHueRange(hue_range)
        self.__lookup_table.SetSaturationRange(1,0)
        self.__lookup_table.SetValueRange(1, 0)
        self.__lookup_table.SetAlphaRange(1, 0)
        self.__lookup_table.SetRange(0, 1)
        self.__lookup_table.Build()


if __name__ == "__main__":
    renderer = WindowRenderer()
    SGVisualiser(renderer.renderer).setup("vtkfiles/density.vtk", (0, 1.0))
    Cone(renderer.renderer).setup_cone(3,5 , 8, (2,2,2), (10,10,1), (0,0,1))
    renderer.setup_render_window()
    renderer.start_render_window()
from vtkmodules.all import(
    vtkActor, vtkPolyDataMapper, vtkActor, vtkCylinderSource, vtkProp
)

from util.window_renderer import WindowRenderer
from vis1 import Cone


class Cylinder:

    def __init__(self, renderer):
        self.__renderer = renderer
        self.__cylinder = vtkCylinderSource()
        self.__cyl_mapper = vtkPolyDataMapper()
        self.__cyl_actor = vtkActor()

    def setup_cylinder_with_diffuse_and_specular(self, radius, height, resolution, center, color ,diffuse, specular, specularpower):

        #Setting the propperty of diffuse and specular
        prop = self.__cyl_actor.GetProperty()
        prop.SetDiffuse(diffuse)
        prop.SetSpecular(specular)
        prop.SetSpecularPower(specularpower)
        self.__cyl_actor.SetProperty(prop)

        #rest of the steps
        self.setup_cylinder(radius,height,resolution,center,color)

    def setup_cylinder(self,radius, height, resolution, center, color):
        # Setup Cylinder size and positioning
        self.__cylinder.SetRadius(radius)
        self.__cylinder.SetHeight(height)
        self.__cylinder.SetResolution(resolution)
        self.__cylinder.SetCenter(center)

        # setup mapper
        self.__cyl_mapper.SetInputConnection(self.__cylinder.GetOutputPort())

        #setup actor
        self.__cyl_actor.SetMapper(self.__cyl_mapper)

        #Setup cylinder color
        self.__cyl_actor.GetProperty().SetColor(color)
        self.__renderer.AddActor(self.__cyl_actor)

if __name__ == '__main__':
    window_renderer = WindowRenderer()
    Cylinder(window_renderer.renderer).setup_cylinder(
        1,3,10, #radius, height, resolution
        (0,0,0), #center
        (1,1,0.4) #color 0-1
    )
    Cylinder(window_renderer.renderer).setup_cylinder_with_diffuse_and_specular(
        1, 3, 10,  # radius, height, resolution
        (4, 0, 0),  # center
        (1, 1, 0.4), # color 0-1
        0.7,
        0.4,
        20
    )
    window_renderer.setup_render_window()
    window_renderer.start_render_window()
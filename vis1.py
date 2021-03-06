from vtkmodules.all import (
    vtkConeSource, vtkPolyDataMapper, vtkActor,
)

from util.window_renderer import WindowRenderer


class Cone:

    def __init__(self, renderer):
        # Renderer variable is needed to add the cone actor
        self.__renderer = renderer

        self.__cone = vtkConeSource()
        self.__cone_mapper = vtkPolyDataMapper()
        self.__cone_actor = vtkActor()

    def setup_cone(self, radius, height, resolution, direction, center, color):
        """Setup the cone"""

        # Set cone
        self.__cone.SetRadius(radius)
        self.__cone.SetHeight(height)
        self.__cone.SetResolution(resolution)
        self.__cone.SetDirection(direction)
        self.__cone.SetCenter(center)

        # Set cone mapper
        self.__cone_mapper.SetInputConnection(self.__cone.GetOutputPort())

        # Set cone actor
        self.__cone_actor.SetMapper(self.__cone_mapper)
        self.__cone_actor.GetProperty().SetColor(color)

        # Add cone actor to the window renderer
        self.__renderer.AddActor(self.__cone_actor)


# Run the program
if __name__ == '__main__':
    window_renderer = WindowRenderer()
    Cone(window_renderer.renderer).setup_cone(
        1.0, 3.0, 40,  # radius, height, resolution
        (0.0, 0.0, 0.0),  # direction
        (0.0, 0.0, 0.0),  # center
        (1.0, 0.0, 0.0)  # color
    )
    Cone(window_renderer.renderer).setup_cone(
        0.5, 2.0, 4,  # radius, height, resolution
        (0.3, 1.0, 0.3),  # direction
        (2.0, 2.0, 2.0),  # center
        (0.0, 1.0, 1.0)  # color
    )

    window_renderer.setup_render_window()
    window_renderer.start_render_window()
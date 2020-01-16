from vtkmodules.all import (
    vtkStructuredPointsReader, vtkFixedPointVolumeRayCastMapper,
    vtkVolumeProperty,
    vtkVolume, vtkFixedPointVolumeRayCastMIPHelper,
)

from util.window_renderer import WindowRenderer

if __name__ == '__main__':
    filename = "objfiles/torso.vtk"
    __window = WindowRenderer()
    __renderer = __window.renderer

    # Read file
    __reader = vtkStructuredPointsReader()
    __reader.SetFileName(filename)
    __reader.Update()

    # Map file
    __mapper = vtkFixedPointVolumeRayCastMapper()
    __mapper.SetInputConnection(__reader.GetOutputPort())
    __mapper.SetBlendModeToMaximumIntensity()

    # Properties shading interpoliation
    __properties = vtkVolumeProperty()
    __properties.ShadeOn()
    __properties.SetInterpolationTypeToLinear()

    # instead of actor use volume pretty much the same methods
    __volume = vtkVolume()
    __volume.SetMapper(__mapper)
    __volume.SetProperty(__properties)

    # not add actor but add volume
    __renderer.AddVolume(__volume)

    # Standard step of window renderer
    __window.setup_render_window()
    __window.start_render_window()
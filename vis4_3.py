from vtkmodules.all import (
    vtkSLCReader, vtkExtractVOI,
    vtkContourFilter, vtkPolyDataMapper,
    vtkProperty, vtkActor,
    vtkOutlineFilter,
    vtkSphere,
    vtkCutter,
    vtkClipDataSet
)

from util.window_renderer import WindowRenderer
#cut is boolean if need to cut
def kneeinner(renderer, zoomlevel, opacity, color):
    reader = vtkSLCReader()
    extracter = vtkExtractVOI()

    contourfilter = vtkContourFilter()
    mapper = vtkPolyDataMapper()
    property = vtkProperty()
    actor = vtkActor()

    outline_filter = vtkOutlineFilter()
    outline_mapper = vtkPolyDataMapper()
    outline_property = vtkProperty()
    outline_actor = vtkActor()

    reader.SetFileName("objfiles/vw_knee.slc")
    reader.Update()

    # Extract volume of interest to subsample the data for faster rendering
    extracter.SetInputConnection(reader.GetOutputPort())
    extracter.SetSampleRate(3, 1, 1)

    # Set contour filter
    contourfilter.SetInputConnection(extracter.GetOutputPort())
    contourfilter.SetValue(0, zoomlevel)


    mapper.SetInputConnection(contourfilter.GetOutputPort())
    mapper.ScalarVisibilityOff()

    # Set property
    property.SetColor(color)
    property.SetOpacity(opacity)

    # Set actor
    actor.SetMapper(mapper)
    actor.SetProperty(property)

    # Set outline filter
    outline_filter.SetInputConnection(extracter.GetOutputPort())

    # Set outline mapper
    outline_mapper.SetInputConnection(outline_filter.GetOutputPort())

    # Set property
    outline_property.SetColor(0.2, 0.2, 0.2)

    # Set outline actor
    outline_actor.SetMapper(outline_mapper)
    outline_actor.SetProperty(outline_property)

    # Add actor to the window renderer
    renderer.AddActor(actor)
    renderer.AddActor(outline_actor)


if __name__ == '__main__':
    window = WindowRenderer()
    renderer = window.renderer


    kneeinner(renderer, 80,1, (1,1,1)) #bone
    kneeinner(renderer, 79,1, (1,1,1)) #bone
    kneeinner(renderer, 78,1, (1,1,1)) #bone
    kneeinner(renderer, 77,1, (1,1,1)) #bone
    kneeinner(renderer, 76,1, (1,1,1)) #bone
    kneeinner(renderer, 75,1, (1,1,1)) #bone
    kneeinner(renderer, 74,1, (1,1,1)) #bone
    kneeinner(renderer, 140,1, (0,0,0)) #InnerBone
    kneeinner(renderer, 90,1, (1,1,1)) #InnerBone
    kneeinner(renderer, 20,0.2,(1, 0.8, 0.4)) #skin
    kneeinner(renderer, 60,0.01,(0, 1, 0)) #skin

    window.setup_render_window()
    window.start_render_window()
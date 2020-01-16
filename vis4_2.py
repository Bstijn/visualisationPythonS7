from vtkmodules.all import (
vtkVolume16Reader, vtkContourFilter, vtkPolyDataMapper, vtkActor, vtkProperty
)
from util.window_renderer import WindowRenderer


def __skin_renderer(renderer):
        __reader = vtkVolume16Reader()
        __reader.SetDataDimensions(64, 64)
        __reader.SetImageRange(1, 93)
        __reader.SetDataByteOrderToLittleEndian()
        __reader.SetFilePrefix("objfiles/headsq/quarter")
        __reader.SetDataSpacing(3.2, 3.2, 1.5)

        __contourfilter = vtkContourFilter()
        __contourfilter.SetInputConnection(__reader.GetOutputPort())
        #__contourfilter.SetValue(0, 1150)
        __contourfilter.SetValue(1, 500)

        __mapper = vtkPolyDataMapper()
        __mapper.SetInputConnection(__contourfilter.GetOutputPort())
        __mapper.ScalarVisibilityOff()

        __prop = vtkProperty()
        __prop.SetDiffuseColor(1, 0.8, 0.4)
        __prop.SetDiffuse(1)
        __prop.SetOpacity(0.2)

        __actor = vtkActor()
        __actor.SetMapper(__mapper)
        __actor.SetProperty(__prop)

        renderer.AddActor(__actor)

def __skull__renderer(renderer):
        __reader = vtkVolume16Reader()
        __reader.SetDataDimensions(64, 64)
        __reader.SetImageRange(1, 93)
        __reader.SetDataByteOrderToLittleEndian()
        __reader.SetFilePrefix("objfiles/headsq/quarter")
        __reader.SetDataSpacing(3.2, 3.2, 1.5)

        __contourfilter = vtkContourFilter()
        __contourfilter.SetInputConnection(__reader.GetOutputPort())
        __contourfilter.SetValue(0, 1150)
        #__contourfilter.SetValue(1, 500)

        __mapper = vtkPolyDataMapper()
        __mapper.SetInputConnection(__contourfilter.GetOutputPort())
        __mapper.ScalarVisibilityOff()

        __prop = vtkProperty()
        __prop.SetDiffuseColor(1, 1, 1)
        __prop.SetDiffuse(1)

        __actor = vtkActor()
        __actor.SetMapper(__mapper)
        __actor.SetProperty(__prop)

        renderer.AddActor(__actor)

if __name__ == '__main__':
        __window = WindowRenderer()
        __renderer = __window.renderer

        __skin_renderer(__renderer)
        __skull__renderer(__renderer)

        __window.setup_render_window()
        __window.start_render_window()
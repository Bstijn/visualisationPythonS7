from vtkmodules.util.numpy_support import (numpy_to_vtk as nptovtk, numpy_to_vtkIdTypeArray )
from vtkmodules.all import (
    vtkUnstructuredGrid,
    vtkPoints,
    vtkActor,
    vtkUnstructuredGridReader,
    vtkDataSetMapper,
    vtkGlyph3D,
    vtkArrowSource,
    vtkPolyDataMapper
)
import numpy as np
from vis2_3 import UGVisualiser
from util.window_renderer import WindowRenderer
if __name__ == '__main__':

    # Read Files
    __vectors = np.loadtxt("util/waarden.txt")
    __coordinaten = np.loadtxt("util/coordinaten.txt")
    cells = nptovtk(__vectors)

    #Create Grid and Points
    __unstructured_grid = vtkUnstructuredGrid()
    __points = vtkPoints()

    # Set Data in points
    __points.SetData(nptovtk(__coordinaten))
    #__points.SetVectors(nptovtk(__vectors))

    # set Points in Grid
    __unstructured_grid.SetPoints(__points)
    print(__points)
    #add array
    __unstructured_grid.GetPointData().SetVectors(nptovtk(__vectors))



    __actor = vtkActor()
    __reader = vtkUnstructuredGridReader()
    __mapper = vtkDataSetMapper()


    __mapper.SetInputData(__unstructured_grid)
    __actor.SetMapper(__mapper)

    #region arrow
    __arrow = vtkArrowSource()
    __arrow.SetTipLength(0.25)
    __arrow.SetTipRadius(0.1)
    __arrow.SetTipResolution(10)


    __glyph = vtkGlyph3D()
    __glyph.SetSourceConnection(__arrow.GetOutputPort())
    __glyph.SetInputData(__unstructured_grid)
    __glyph.SetVectorModeToUseVector()
    __glyph.SetColorModeToColorByScalar()
    __glyph.SetScaleModeToDataScalingOff()
    __glyph.OrientOn()
    __glyph.SetScaleFactor(0.2)

    __arrowactor = vtkActor()
    __arrowmapper = vtkDataSetMapper()
    __arrowmapper.SetInputConnection(__glyph.GetOutputPort())
    __arrowmapper.SetScalarRange(0.0, 1.0)
    __arrowmapper.ScalarVisibilityOn()
    __arrowmapper.Update()

    __arrowactor.SetMapper(__arrowmapper)
    #end region arrow


    renderer = WindowRenderer()
    renderer.renderer.AddActor(__actor)
    renderer.renderer.AddActor(__arrowactor)
    renderer.setup_render_window()
    renderer.start_render_window()



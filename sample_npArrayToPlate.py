import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import NumpyArrayToPlate

plateData = np.array([[True,False,True],
    [True,False,True],
    [True,True,True,],
    [False,False,True],
    [False,False,True],])

curMesh = NumpyArrayToPlate.NumpyBoolArrayToPlate(plateData)

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(curMesh.vectors))

# Auto scale to the mesh size
scale = curMesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()
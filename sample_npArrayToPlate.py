import numpy as np
from stl import mesh
import matplotlib
matplotlib.use('Qt5Agg')
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from HolePlateMaker import NumpyArrayToPlate

# 
pyplot.rcParams["font.family"] = "Arial" 

plateData = np.array([[True,False,True],
    [True,False,True],
    [True,True,True,],
    [False,False,True],
    [False,False,True],])

curMesh = NumpyArrayToPlate.NumpyBoolArrayToPlate(plateData)
curMesh.save('plate.stl')

figure = pyplot.figure()
axes = figure.add_subplot(111, projection='3d')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(curMesh.vectors))

# Auto scale to the mesh size
scale = curMesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()
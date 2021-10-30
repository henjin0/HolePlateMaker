import numpy as np
from stl import mesh
import matplotlib
matplotlib.use('Qt5Agg')
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from HolePlateMaker import NumpyArrayToHolePlate

# 
pyplot.rcParams["font.family"] = "Arial" 

plateData = np.array([[1,0,2],
    [2,0,1],
    [1,1,1,],
    [0,0,2],
    [0,0,1],])

curMesh = NumpyArrayToHolePlate.NumpyArrayToPlate(plateData,'4.8mm')
curMesh.save('plate.stl')

figure = pyplot.figure()
axes = figure.add_subplot(111, projection='3d')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(curMesh.vectors))

# Auto scale to the mesh size
scale = curMesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()
import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from mesh_scale import mesh_scale
from mesh_update import mesh_update
from cube_model import cube_model
from mesh_location_zero import mesh_location_zero
from setBU32 import setBU32
from addBlock import addBlock


curMesh = setBU32(0,0,0)
for i in range(1,10):
    for j in range(0,i+1):
        newMesh = setBU32(i,j,0)
        curMesh = addBlock(curMesh, newMesh)

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(curMesh.vectors))

# Auto scale to the mesh size
scale = curMesh.points.flatten()
print(curMesh.min_)
print(curMesh.max_)
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()

curMesh.save('myPlate.stl')
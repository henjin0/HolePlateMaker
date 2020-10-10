import numpy as np
from stl import mesh
from mesh_scale import mesh_scale
from mesh_update import mesh_update
from mesh_location_zero import mesh_location_zero

def setBU32(xPoint,yPoint,zPoint):
    # Using an existing stl file:
    your_mesh = mesh.Mesh.from_file('BU3.2mm.stl')
    your_mesh = mesh_location_zero(your_mesh)
    your_mesh = mesh_update(your_mesh)
    your_mesh.translate(np.array([xPoint*5,yPoint*5,zPoint*3]))
    your_mesh = mesh_update(your_mesh)

    return your_mesh
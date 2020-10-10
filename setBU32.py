import numpy as np
from stl import mesh
import mesh_scale as m_s
import mesh_update as m_u
import mesh_location_zero as m_l_z

def setBU32(xPoint,yPoint,zPoint):
    your_mesh = mesh.Mesh.from_file('BU3.2mm.stl')
    your_mesh = m_l_z.mesh_location_zero(your_mesh)
    your_mesh = m_u.mesh_update(your_mesh)
    your_mesh.translate(np.array([xPoint*5,yPoint*5,zPoint*3]))
    your_mesh = m_u.mesh_update(your_mesh)

    return your_mesh
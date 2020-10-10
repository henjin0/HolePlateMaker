import numpy as np
from stl import mesh
from setBU32 import setBU32
from addBlock import addBlock


def NumpyBoolArrayToPlate(plateData):
    size = plateData.shape
    curMesh = mesh.Mesh(np.array([], dtype=mesh.Mesh.dtype))
    for i in np.arange(0,size[0]):
        for j in np.arange(0,size[1]):
            if(plateData[i][j]):
                newMesh = setBU32(i,j,0)
                curMesh = addBlock(curMesh, newMesh)
    
    return curMesh

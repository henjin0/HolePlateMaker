import numpy as np
from stl import mesh
from HolePlateMaker import NumpyArrayToHolePlate

plateData = np.array([[2,0,1],
    [1,0,2],
    [1,2,2,],
    [0,0,1],
    [0,0,2],])

curMesh = NumpyArrayToHolePlate.NumpyArrayToPlate(plateData,'4.8mm')
curMesh.save('example2.stl')
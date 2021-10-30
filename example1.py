import numpy as np
from stl import mesh
from HolePlateMaker import NumpyArrayToHolePlate

plateData = np.array([[1,0,1],
    [1,0,1],
    [1,1,1,],
    [0,0,1],
    [0,0,1],])

curMesh = NumpyArrayToHolePlate.NumpyArrayToPlate(plateData,'3mm')
curMesh.save('example1.stl')
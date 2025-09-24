import numpy as np

array_1 = np.arange(10)

array_2 = np.arange(25).reshape((5,5))

array_3 = np.arange(16).reshape((4,4))
array_4 = np.array(list(reversed(np.arange(16)))).reshape((4,4))

array_5 = np.zeros((11,11))
array_5[2,2]=1
array_5[2,8]=1
array_5[4,5]=1
array_5[6,2]=1
array_5[7,3]=1
array_5[8,4]=1
array_5[8,5]=1
array_5[8,6]=1
array_5[7,7]=1
array_5[6,8]=1
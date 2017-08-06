import numpy as np

a = np.array([[1, 2], [3, 4]])

# repeat each element 3 times
#print(np.repeat(a, 3))
# tile the matrix 3 times
#print(np.tile(a, 3))
#
b = np.array([[5, 6]])
#print(np.concatenate((a, b), axis=0)) #axis=0 !!!
print(np.vstack((a,b))) #vertical stack
print(np.hstack((a,b.T))) #horizontal stack
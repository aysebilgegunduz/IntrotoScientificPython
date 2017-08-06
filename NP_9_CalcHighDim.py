import numpy as np

#m = np.random.rand(3,3)
#print(m)
#print(m.max())
#print(m.max(axis=0)) #column
#print(m.max(axis=1)) #row

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
# #
n, m = A.shape
#
B = A.reshape((1,n*m))
#print(B)
#B[0,0:5] = 5 # modify the array
print(B)
print(A)
# #
C = A.flatten()
print(C)
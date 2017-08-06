import numpy as np

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])

v1 = np.arange(0, 5)

#print(np.dot(A, A)) #array uzerinden matris carpimi
#print(np.dot(A, v1)) #alignment'i kendisi yaparak matris carpimi
#
M = np.matrix(A) #change the behaviour of A
v = np.matrix(v1).T # make it a column vector
#print(A*A)
print(M*v)
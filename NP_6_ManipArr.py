import numpy as np

M = np.random.rand(3,3)

#print(M)
#print(M[1])
#print(M[1,1])
#print(M[1,:]) #row 1
#print(M[:,1]) #column 1
#
A = np.array([1,2,3,4,5])
#print(A[1:3])
#print(A[::2])
#print(A[-1])


############### FANCY INDEXING #####################

# A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
# print(A)
# row_indices = [1, 2, 3]
# print(A[row_indices])
# col_indices = [1, 2, -1]
# print(A[row_indices,col_indices])
#
which = [1, 0, 1, 0,2]
choices = [[-2,-2,-2,3,8], [5,5,4,5,8],[9,9,9,9,9]]
# # #Constructs an array by picking elements from several arrays
print(np.choose(which, choices))
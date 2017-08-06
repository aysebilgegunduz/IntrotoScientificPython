import numpy as np

################### ARANGE ############################
#create a range
x1 = np.arange(0,10,1) #arguments:start,stop,step
x2 = np.arange(-1,1,0.1)
#print(x1)
#print(x2)

################### LINSPACE - LOGSPACE ###############
l1 = np.linspace(0,10,10) #starts and end points are included
l2 = np.logspace(0,10,10,base=2)
#print(l1)
#print(l2)

################### MGRID ############################
#mesh grid
x,y = np.mgrid[0:5, 0:5]

print(x)
print(y)
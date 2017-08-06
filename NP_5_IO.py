import numpy as np
import matplotlib.pyplot as plt

# data = np.genfromtxt('stockholm_td_adj.dat')
# #print(data.shape)
#
# fig, ax = plt.subplots(figsize=(14,4))
#
# ax.plot(data[:,0]+data[:,1]/12.0+data[:,2]/365, data[:,5])
# ax.axis('tight')
# ax.set_title('tempeatures in Stockholm')
# ax.set_xlabel('year')
# ax.set_ylabel('temperature (C)')
# plt.show(fig)

m = np.random.rand(3,4)
np.savetxt("deneme.csv", m)

print(m)
print(m.itemsize) #bytes per element
print(m.nbytes) #number of bytes
print(m.ndim) #number of dimensions
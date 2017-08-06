from pylab import *
import numpy as np
x = np.linspace(0, 5, 10)
y = x ** 2

#instead of one by one import pylab
subplot(1,2,1)
plot(x, y, 'r--')
subplot(1,2,2)
plot(y, x, 'g*-');
show()
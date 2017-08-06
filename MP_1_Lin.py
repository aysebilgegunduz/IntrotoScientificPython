import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 10)
y = x ** 2

plt.figure()
plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title')
plt.show()
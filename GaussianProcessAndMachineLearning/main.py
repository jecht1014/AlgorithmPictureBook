import numpy as np
import matplotlib.pyplot as plt

#from linear_regression import *
from linear_regression import *
x = np.random.normal(0, 1, 10)
epsilon = np.random.normal(0, 0.1, 10)
a = 1
b = 1/2
y = a + x*b + epsilon

x2 = np.arange(-2, 3)
y2 = a + x2 * b

a2, b2 = simple_regression(x, y)
y3 = a2 + x2 * b2

print('real:', a, b, ' prediction:', a2, b2)

plt.scatter(x, y)
plt.plot(x2, y2)
plt.plot(x2, y3)
plt.legend(['real', 'prediction'])
plt.show()
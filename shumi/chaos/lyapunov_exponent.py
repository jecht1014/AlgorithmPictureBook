import math
def lyapunov_exponent(d):
    lamb = 0
    for i in range(len(d)-2):
        lamb += math.log((abs(d[i+2]-d[i+1])+1e-17)/(abs(d[i+1]-d[i])+1e-17))
    lamb /= len(d)
    return lamb
def logistic_f(alpfa, x0, n):
    y = [0] * n
    y[0] = x0
    x = x0
    for i in range(1, n):
        x = alpfa*x*(1-x)
        y[i] = x
    return y

import matplotlib.pyplot as plt
import numpy as np
r = 1000
x = np.linspace(1, 4, r)
y = [0] * r
for i in range(r):
    y[i] = lyapunov_exponent(logistic_f(x[i], 0.001, 10000))
plt.xlabel('alpha')
plt.ylabel('lyapunov_exponent')
plt.plot(list(x), y)
plt.savefig('image/lyapunov_exponent_logistic.png')
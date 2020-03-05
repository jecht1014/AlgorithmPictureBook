def logistic_f(alpfa, x0, n):
    y = [0] * n
    y[0] = x0
    x = x0
    for i in range(1, n):
        x = alpfa*x*(1-x)
        y[i] = x
    return y

import matplotlib.pyplot as plt
x_range = 100
alpha = 3.5
y = logistic_f(alpha, 0.001, x_range)
x = list(range(1, x_range+1))
plt.plot(x, y)
plt.savefig('image/logistic_function_alpha{0}.png'.format(alpha))
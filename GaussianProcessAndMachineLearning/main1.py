import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from gaussian_def.linear_regression import *

def simple_regression_plot(a, b, n = 10):
    x = np.random.normal(0, 1, n)
    epsilon = np.random.normal(0, 0.1, 10)
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

def multiple_regression3d_plot(w, n = 10):
    x = np.random.normal(0, 1, (n, 2))
    x_1 = np.ones((n, 1))
    X = np.hstack((x_1, x))
    epsilon = np.random.normal(0, 0.1, (n, 1))
    y = np.dot(X, w) + epsilon

    x2_1 = np.arange(-2.0, 2.0, 0.5)
    x2_2 = np.arange(-2.0, 2.0, 0.5)
    x2_1, x2_2 = np.meshgrid(x2_1, x2_2)
    y2 = w[0, 0] + w[1, 0] * x2_1 + w[2, 0] * x2_2

    prediction_w = multiple_regression(X, y)
    y3 = prediction_w[0, 0] + prediction_w[1, 0] * x2_1 + prediction_w[2, 0] * x2_2

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('f(x1, x2)')
    ax.plot_wireframe(x2_1, x2_2, y2)
    ax.plot_wireframe(x2_1, x2_2, y3)
    ax.plot(x[:, 0], x[:, 1], y[0, :], marker = 'o', linestyle = 'None')
    plt.show()

def x_to_function(x):
    x1 = np.ones_like(x)
    x2 = np.hstack((x1, x))
    x3 = np.hstack((x2, np.square(x)))
    x4 = np.hstack((x3, np.sin(x)))
    x5 = np.hstack((x4, np.cos(x)))
    return x5

def linear_regression2d_plot(w, n = 10):
    x1 = np.random.normal(0, 3, (n, 1))
    phi = x_to_function(x1)
    epsilon = np.random.normal(0, 1, n)
    y = np.dot(phi, w) + epsilon

    x2 = np.arange(-6.0, 6.0, 0.5)
    x2 = np.reshape(x2, (x2.shape[0], 1))
    phi2 = x_to_function(x2)
    y2 = np.dot(phi2, w)

    prediction_w = linear_regression(phi, y)
    y3 = np.dot(phi2, prediction_w)
    print(prediction_w)
    
    plt.scatter(x1, y)
    plt.plot(x2, y2)
    plt.plot(x2, y3)
    plt.show()

'''
a = 1
b = 1
simple_regression_plot(a, b, n = 10)
w = np.array([[0.5, 1, 1]]).T
multiple_regression3d_plot(w, n = 10)

w = np.array([1, 6, -1, 2, -1])
linear_regression2d_plot(w)
'''

X = np.array([[1, 2, 4], [1, 3, 6.1], [1, 4, 7.9]])
y = np.array([[3], [5], [8]])
w = ridge_regression(X, y)
print(w)
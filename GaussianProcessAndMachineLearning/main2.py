import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

from gaussian_def.gaussian_distribution import *

def gaussian_probability_density_plot(mu = 0, sigma2 = 1):
    x = np.arange(-5, 5, 0.1)
    y = gaussian_probability_density(x)

    plt.plot(x, y)
    #plt.savefig('image/chapter2/gaussian_probability_density.png')
    plt.show()

def box_muller_plot(n, mu = 0, sigma2 = 1):
    y = np.ones(n)
    x = np.array([box_muller(mu = mu, sigma2 = sigma2) for i in range(n)])

    plt.hist(x)
    #plt.savefig('image/chapter2/box_muller.png')
    plt.show()

def multivariate_gaussian_probability_density_plot3d():
    x1_1 = np.arange(-2.0, 2.0, 0.1)
    x1_2 = np.arange(-2.0, 2.0, 0.1)
    x1_1, x1_2 = np.meshgrid(x1_1, x1_2)
    s = x1_1.shape
    x2_1 = np.reshape(x1_1, (1, s[0] * s[1]))
    x2_2 = np.reshape(x1_2, (1, s[0] * s[1]))
    x = np.vstack([x2_1, x2_2])
    mu = np.array([[0], [0]])
    sigma = np.array([[1, 0], [0, 1]])
    n = np.array([])
    for i in range(x.shape[1]):
        n = np.append(n, multivariate_gaussian_probability_density(np.reshape(x[:, i], (2, 1)), mu, sigma))
    n = np.reshape(n, s)

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('n')
    ax.plot_wireframe(x1_1, x1_2, n)
    #plt.savefig('image/chapter2/multivariate_gaussian_probability_density3d.png')
    plt.show()

gaussian_probability_density_plot()
box_muller_plot(10000)
multivariate_gaussian_probability_density_plot3d()
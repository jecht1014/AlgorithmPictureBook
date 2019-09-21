import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def old_waveletf(x, a = None):
    if a == None:
        l = np.random.normal(0, 3, 1) * x
    elif a == True:
        l = 1
    else:
        l = a * x
    y = (1 -3 * np.power(x, 2) + 2 * np.abs(np.power(x, 3))) * l
    return y

def new_waveletf(x, a = None):
    if a == None:
        l = np.random.normal(0, 3, 1) * x
    elif a == True:
        l = 1
    else:
        l = a * x
    y = (1 - (6 * np.abs(np.power(x, 5)) -15 * np.power(x, 4) + 10 * np.abs(np.power(x, 3)))) * l
    return y

def set_perlin_noise1d(n = 5, plot_judge = False):
    x = np.linspace(-1, 1, 51)
    y = np.array([])
    
    y_left = new_waveletf(x)
    for _ in range(n):
        y_right = new_waveletf(x)
        y = np.hstack([y, y_left[26:] + y_right[1:26]])
        y_left = y_right
    
    if plot_judge:
        x = np.linspace(0, n, n * 25)
        plt.plot(x, y)
        plt.show()

    return y

def waveletf2d(x, y, a = True):
    c1 = new_waveletf(x, a)
    c2 = new_waveletf(y, a)

    z = c1 * c2 * (np.random.normal(0, 3, 1)*x + np.random.normal(0, 3, 1)*y)
    return z

def plot_waveletf():
    x = np.linspace(-1, 1, 50)
    parlin_noise = new_waveletf(x)

    plt.plot(x, parlin_noise)
    plt.show()

def plot_perlin_noise1d():
    x = np.linspace(-1, 1, 51)
    y_left = new_waveletf(x)
    y_right = new_waveletf(x)

    plt.plot(np.linspace(-1, 1, 51), y_left)
    plt.plot(np.linspace(0, 2, 51), y_right)
    plt.plot(np.linspace(0, 1, 26), y_left[25:] + y_right[:26])
    plt.show()

def plot_wavelet2d():
    u = np.linspace(-1, 1, 51)
    v = np.linspace(-1, 1, 51)
    u, v = np.meshgrid(u, v)
    y = waveletf2d(u, v)

    plt.pcolormesh(u, v, y, cmap='Greys')
    plt.colorbar(orientation="vertical")
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(u, v, y, cmap='bwr', linewidth=0)
    fig.colorbar(surf)
    ax.set_title("Surface Plot")
    '''
    plt.show()

def plot_perlin_noise2d():
    sep = 51
    u1 = np.linspace(0, 1, sep)
    v1 = np.linspace(0, 1, sep)
    u1, v1 = np.meshgrid(u1, v1)
    y1 = waveletf2d(u1, v1)

    u2 = np.linspace(-1, 0, sep)
    v2 = np.linspace(0, 1, sep)
    u2, v2 = np.meshgrid(u2, v2)
    y2 = waveletf2d(u2, v2)

    u3 = np.linspace(0, 1, sep)
    v3 = np.linspace(-1, 0, sep)
    u3, v3 = np.meshgrid(u3, v3)
    y3 = waveletf2d(u3, v3)

    u4 = np.linspace(-1, 0, sep)
    v4 = np.linspace(-1, 0, sep)
    u4, v4 = np.meshgrid(u4, v4)
    y4 = waveletf2d(u4, v4)

    plt.pcolormesh(u1, v1, y1+y2+y3+y4, cmap='Greys')
    plt.colorbar(orientation="vertical")
    plt.show()

#a = set_perlin_noise(10, True)
plot_perlin_noise2d()
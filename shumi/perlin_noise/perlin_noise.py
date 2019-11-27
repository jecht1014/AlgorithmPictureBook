import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def a_function(direction_num = None):
    if direction_num == None:
        a = np.random.normal(0, 3, 1)
    elif direction_num == 4:
        a = np.random.rand()
        if a < 0.25:
            a = 1 / 1000
        elif a < 0.5:
            a = 1000
        elif a < 0.75:
            a = -1 / 1000
        else:
            a = -1000
    elif direction_num == 8:
        a = np.random.rand()
        if a < 0.125:
            a = 1 / 1000
        elif a < 0.25:
            a = 1
        elif a < 0.375:
            a = 1000
        elif a < 0.5:
            a = -1
        elif a < 0.625:
            a = -1 / 1000
        elif a < 0.75:
            a = 1
        elif a < 0.875:
            a = -1000
        else:
            a = -1
    return a

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

def waveletf2d(x, y, direction_num = None, a = True):
    c1 = new_waveletf(x, a)
    c2 = new_waveletf(y, a)

    z = c1 * c2 * (a_function(direction_num = direction_num)*x + a_function(direction_num = direction_num)*y)
    return z

def set_perlin_noise2d(n, sep = 51, direction_num = None, plot_judge = False):
    u = np.linspace(-1, 1, sep)
    v = np.linspace(-1, 1, sep)
    u, v = np.meshgrid(u, v)
    z = np.zeros(((n+1) * int(sep/2) + 1, (n+1) * int(sep/2) + 1))

    for i in range(n):
        for j in range(n):
            z[i*int(sep/2):i*int(sep/2)+sep, j*int(sep/2):j*int(sep/2)+sep] += waveletf2d(u, v, direction_num = direction_num)
 
    x = np.linspace(0, n-1, int(sep/2) * (n-1) + 1)
    y = np.linspace(0, n-1, int(sep/2) * (n-1) + 1)
    x, y = np.meshgrid(x, y)

    if plot_judge:
        plt.pcolormesh(x, y, z[int(sep/2):int(sep/2) * n + 1, int(sep/2):int(sep/2) * n + 1], cmap='Greys')
        plt.colorbar(orientation="vertical")
        plt.show()
    return z[int(sep/2):int(sep/2) * n + 1, int(sep/2):int(sep/2) * n + 1]

def fractal_perlin_noise2d(fractal_num = 7, direction_num = None, plot_way = '3d'):
    sep = 16 * (2**fractal_num)
    x = np.linspace(0, 1, int(sep/2)+1)
    y = np.linspace(0, 1, int(sep/2)+1)
    x, y = np.meshgrid(x, y)
    for i in range(fractal_num):
        if i == 0:
            z = set_perlin_noise2d(n = 2 ** (i+1), sep = int(sep / (2 ** i)) +1, direction_num = None)
        else:
            z += set_perlin_noise2d(n = 2 ** (i+1), sep = int(sep / (2 ** i)) +1, direction_num = None)[:z.shape[0], :z.shape[1]]

    z = z / fractal_num

    if plot_way == '2d':
        plt.pcolormesh(x, y, z, cmap='Greys')
        plt.colorbar(orientation="vertical")
        plt.show()
    elif plot_way == '3d':
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(x, y, z, cmap='bwr', linewidth=0)
        fig.colorbar(surf)
        ax.set_title("Surface Plot")
        plt.show()

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
#set_perlin_noise2d(5, direction_num=8, plot_judge = True)
a = fractal_perlin_noise2d()
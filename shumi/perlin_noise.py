import numpy as np
import matplotlib.pyplot as plt

def waveletf(x, a = None):
    if a == None:
        l = np.random.normal(0, 3, 1) * x
    else:
        l = a * x
    y = (1 -3 * np.power(x, 2) + 2 * np.abs(np.power(x, 3))) * l
    return y

def perlin_noise_plot():
    x = np.linspace(-1, 1, 51)
    y_left = waveletf(x)
    y_right = waveletf(x)

    plt.plot(np.linspace(-1, 1, 51), y_left)
    plt.plot(np.linspace(0, 2, 51), y_right)
    plt.plot(np.linspace(0, 1, 26), y_left[25:] + y_right[:26])
    plt.show()

def set_perlin_noise(n = 5, plot_judge = False):
    x = np.linspace(-1, 1, 51)
    y = np.array([])
    
    y_left = waveletf(x)
    for _ in range(n):
        y_right = waveletf(x)
        y = np.hstack([y, y_left[26:] + y_right[1:26]])
        y_left = y_right
    
    if plot_judge:
        x = np.linspace(0, n, n * 25)
        plt.plot(x, y)
        plt.show()

    return y

def plot_waceletf():
    x = np.linspace(-1, 1, 50)
    parlin_noise = waveletf(x)

    plt.plot(x, parlin_noise)
    plt.show()

ra = set_perlin_noise(10, True)
import numpy as np
import matplotlib.pyplot as plt
from gaussian_distribution import *


def gaussian_probability_density_plot(mu = 0, sigma2 = 1):
    x = np.arange(-5, 5, 0.1)
    y = gaussian_probability_density(x)

    plt.plot(x, y)
    plt.show()

gaussian_probability_density_plot()
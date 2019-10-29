import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
from gaussian_def.gaussian_process import *

def rbf_plot():
    #x = np.linspace(-5, 5, 50)
    x = np.arange(0, 5, 0.2) + 1
    x2 = np.reshape(x, (x.shape[0], 1))
    k = rbf(x2)
    r = np.reshape(mvnrnd(k), (x.shape[0]))
    
    plt.subplot(1,2,1)
    plt.plot(x, r.T)
    plt.subplot(1,2,2)
    plt.imshow(k, cmap = 'Greys')
    plt.show()

rbf_plot()
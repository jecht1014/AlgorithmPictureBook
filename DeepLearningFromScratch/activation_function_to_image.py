import numpy as np
import matplotlib.pylab as plt
from nn.activation_function import *

save_path = 'image/activation_function'
x = np.arange(-5.0, 5.0, 0.01)
y = sigmoid(x)
plt.plot(x, y)
plt.savefig(save_path + '/sigmoid.png')
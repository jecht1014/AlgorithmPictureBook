import math
import numpy as np
import math
import copy
import matplotlib.pyplot as plt

def get_distance(coordinate1, coordinate2):
    result = 0
    for i in range(len(coordinate1)):
        result += math.pow(coordinate1[i]-coordinate2[i], 2)
    result = math.pow(result, 0.5)
    return result

def get_degree(coordinate1, coordinate2):
    y = coordinate2[1]-coordinate1[1]
    x = coordinate2[0]-coordinate1[0]
    return math.atan2(y, x)

def koch_curve(basic_line, curve, fractal_num):
    basic_line = np.array(basic_line)
    curve = np.array(curve)
    next_line = copy.deepcopy(basic_line)
    for num in range(fractal_num):
        line = copy.deepcopy(next_line)
        next_line = np.array([line[0]])
        for i in range(len(line)-1):
            dist_basic_line = get_distance(line[i], line[i+1])
            dist_curve = get_distance(curve[0], curve[curve.shape[0]-1])
            frac = curve / dist_curve * dist_basic_line

            deg = get_degree(line[i], line[i+1])
            x = frac[:, 0]*np.cos(deg) - frac[:, 1]*np.sin(deg) + line[i, 0]
            y = frac[:, 0]*np.sin(deg) + frac[:, 1]*np.cos(deg) + line[i, 1]
            new_frac = np.stack([x, y]).T

            next_line = np.vstack([next_line, new_frac[1:]])
    return next_line

save_path = 'image'
basic_line = [[0, 0], [3, 0]]
curve = [[0, 0], [1, 0], [1.5, 0.5*math.sqrt(3)], [2, 0], [3, 0]]
#curve = [[0, 0], [1, 0], [1.5, 0.5*math.sqrt(3)], [2, 0], [3, 0], [3.5, -0.5*math.sqrt(3)], [4, 0], [5, 0]]
fractal = koch_curve(basic_line, curve, 6)

plt.plot(fractal[:, 0], fractal[:, 1])
plt.xticks(np.arange(0, 3.1, 0.5))
plt.yticks(np.arange(0, 3.1, 0.5))
plt.savefig(save_path + '/koch_curve6')
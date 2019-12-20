import random
import matplotlib.pyplot as plt
import copy
import numpy as np

def midpoint_displacement_method(basic_line, displace_num, a=0.8):
    for n in range(displace_num):
        next_line = [basic_line[0]]
        for i in range(len(basic_line)-1):
            x = (basic_line[i][0]+basic_line[i+1][0]) / 2
            y = (basic_line[i][1]+basic_line[i+1][1]) / 2 + pow(a, n) * random.random() * pow(-1, int(random.random()+0.5))
            next_line.append([x, y])
            next_line.append(basic_line[i+1])
        basic_line = copy.deepcopy(next_line)
    return basic_line

basic_line = [[0, 0], [4, 0]]
line = midpoint_displacement_method(basic_line, 9)
line = np.array(line)

plt.plot(line[:, 0], line[:, 1])
plt.show()
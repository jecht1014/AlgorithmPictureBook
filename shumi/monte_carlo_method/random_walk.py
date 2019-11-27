import numpy as np
import matplotlib.pyplot as plt
import random

save_path = 'image'
walk_times = 3
random_walk_times = 100000
count = np.zeros(((walk_times+1)*2, (walk_times+1)*2))
for i in range(random_walk_times):
    x = walk_times
    y = walk_times
    for j in range(walk_times):
        r = random.random()
        if (r < 0.25):
            y -= 1
        elif (0.25 <= r < 0.5):
            x += 1
        elif (0.5 <= r < 0.75):
            y += 1
        else:
            x -= 1
    count[x][y] += 1

X,Y = np.meshgrid(np.arange(count.shape[1]),np.arange(count.shape[0]))
plt.pcolormesh(X, Y, count, cmap='Greys')
plt.savefig(save_path+'/random_walk{}.png'.format(walk_times))
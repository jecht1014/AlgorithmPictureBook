import numpy as np
import matplotlib.pyplot as plt
import random

save_path = 'image'
walk_times = 20
reflective_wall = 4
random_walk_times = 100000
count = np.zeros(((reflective_wall+1)*2, (reflective_wall+1)*2))
for i in range(random_walk_times):
    x = reflective_wall
    y = reflective_wall
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

        # 反射壁に沿ってる場合動かない確率が0.25
        if (x >= reflective_wall*2+1):
            x -= 1
        elif (y >= reflective_wall*2+1):
            y -= 1
        elif (x < 0):
            x += 1
        elif (y < 0):
            y += 1
    count[x][y] += 1

X,Y = np.meshgrid(np.arange(count.shape[1]),np.arange(count.shape[0]))
plt.pcolormesh(X, Y, count, cmap='Greys')
plt.savefig(save_path+'/random_walk_plus_rw2-{0}-{1}.png'.format(walk_times, reflective_wall))
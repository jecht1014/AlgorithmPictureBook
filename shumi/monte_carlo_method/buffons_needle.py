import random
import math

monte_carlo_times = 1000000
count = 0
l = 1
a = 1
for i in range(monte_carlo_times):
    m = random.random() * a
    theta = random.random() * (math.pi/2)
    if (l*math.cos(theta) + m >= a):
        count += 1
print('pi:{0} prediction:{1}'.format(math.pi, 2*l / (a * count/monte_carlo_times)))
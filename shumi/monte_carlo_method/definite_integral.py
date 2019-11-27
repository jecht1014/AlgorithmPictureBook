import math
import random
import numpy as np

def numerical_integration(sequence):
    result = 0
    for i in range(len(sequence)-1):
        result += (math.cos(sequence[i])+math.cos(sequence[i+1])) * (sequence[i+1]-sequence[i]) / 2
    return result

sequence = np.linspace(0, math.pi/2, 10000)
num_integ = numerical_integration(sequence.tolist())

monte_carlo_times = 1000000
count = 0
for i in range(monte_carlo_times):
    if (random.random() <= math.cos(random.random()*math.pi/2)):
        count += 1
print('numerical_integration:{0} monte_carlo:{1}'.format(num_integ, count/monte_carlo_times * math.pi/2))
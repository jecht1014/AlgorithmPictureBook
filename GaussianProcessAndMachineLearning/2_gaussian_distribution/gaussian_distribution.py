import numpy as np
import random
import math

def gaussian_probability_density(x, mu = 0, sigma2 = 1):
    return (1 / np.sqrt(2*np.pi) * sigma2) * np.exp(-np.power(x - mu, 2) / 2 * sigma2)

def box_muller(mu = 0, sigma2 = 1):
    return mu + sigma2 * (math.sqrt(-2 * math.log(random.random())) * math.sin(2 * math.pi * random.random()))
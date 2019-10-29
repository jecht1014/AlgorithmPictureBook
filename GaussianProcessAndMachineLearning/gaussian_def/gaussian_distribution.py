# chapter2
import numpy as np
import random
import math

def gaussian_probability_density(x, mu = 0, sigma2 = 1):
    return (1 / np.sqrt(2*np.pi* sigma2)) * np.exp(-np.power(x - mu, 2) / 2 * sigma2)

def box_muller(mu = 0, sigma2 = 1):
    return mu + sigma2 * (math.sqrt(-2 * math.log(random.random())) * math.sin(2 * math.pi * random.random()))

# mu:xの平均値ベクトル, sigma:共分散行列
def multivariate_gaussian_probability_density(x, mu, sigma):
    normalization_constant = 1 / (np.power(np.sqrt(2 * np.pi), sigma.shape[0]) * np.sqrt(np.linalg.det(sigma)))
    return normalization_constant * np.exp(-1 / 2 * np.dot(np.dot((x - mu).T, np.linalg.inv(sigma)), (x - mu)))
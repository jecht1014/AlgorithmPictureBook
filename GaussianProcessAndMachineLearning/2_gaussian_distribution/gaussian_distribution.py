import numpy as np
def gaussian_probability_density(x, mu = 0, sigma2 = 1):
   return (1 / np.sqrt(2*np.pi) * sigma2) * np.exp(-np.power(x - mu, 2) / 2 * sigma2)
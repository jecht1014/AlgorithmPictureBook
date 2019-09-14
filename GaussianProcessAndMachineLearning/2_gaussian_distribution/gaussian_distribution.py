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

# 平均0の多変量正規乱数の作成
def mvnrnd(sigma):
    l = np.linalg.cholesky(sigma)
    r = np.array([])
    for _ in range(sigma.shape[0]):
        r = np.append(r, box_muller())
    y = np.reshape(np.dot(l, r), (sigma.shape[0], 1))
    return y

# ガウスカーネル関数
def gbf(x, theta1 = 1, theta2 = 1):
    x2 = np.tile(x.T, (x.shape[0], 1))
    k = theta1 * np.exp(-np.power(x2 - x, 2) / theta2)
    return k
# chapter3
import numpy as np

import sys
import os
sys.path.append(os.getcwd())
from gaussian_def.gaussian_distribution import *

# 平均0の多変量正規乱数の作成
def mvnrnd(sigma):
    l = np.linalg.cholesky(sigma)
    r = np.array([])
    for _ in range(sigma.shape[0]):
        r = np.append(r, box_muller())
    y = np.reshape(np.dot(l, r), (sigma.shape[0], 1))
    return y

# ガウスカーネル関数
def rbf(x1, x2, theta1 = 1, theta2 = 1):
    return theta1 * np.exp(-np.power(x2 - x1, 2) / theta2)

# 線形カーネル関数
def linear_kernel(x1, x2):
    return x1*x2

# 指数カーネル関数
def exponential_kernel(x1, x2, theta = 1):
    return np.exp(-np.abs(x1 - x2) / theta)

# 周期カーネル
def periodic_kernel(x1, x2, theta1 = 1, theta2 = 1):
    return np.exp(theta1 * np.cos(np.abs(x1-x2) / theta2))

# カーネルで共分散行列の作製
def make_k(x, kernel):
    x2 = np.tile(x.T, (x.shape[0], 1))
    k = kernel(x, x2)
    return k

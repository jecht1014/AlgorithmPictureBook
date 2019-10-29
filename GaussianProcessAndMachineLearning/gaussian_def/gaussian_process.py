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
def rbf(x, theta1 = 1, theta2 = 1):
    x2 = np.tile(x.T, (x.shape[0], 1))
    k = theta1 * np.exp(-np.power(x2 - x, 2) / theta2)
    return k
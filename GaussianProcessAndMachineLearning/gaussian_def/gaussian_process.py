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
def make_k(x, sigma2, kernel):
    x2 = np.tile(x.T, (x.shape[0], 1))
    k = kernel(x, x2) + sigma2 * np.eye(x2.shape[0])
    return k

# ガウス過程回帰
def gaussian_process(xtrain, xtest, ytrain, ytest, sigma2, kernel = rbf):
    K = make_k(xtrain, sigma2, kernel)
    k = np.zeros((1, ytrain.shape[0]))
    Kinv = np.linalg.inv(K)

    mu = np.zeros(ytest.shape[0])
    var = np.zeros(ytest.shape[0])
    for i in range(ytest.shape[0]):
        for j in range(ytrain.shape[0]):
            k[0][j] = kernel(xtrain[j], xtest[i])
        s = kernel(xtest[i], xtest[i]) + sigma2
        mu[i] = (k.dot(Kinv).dot(ytrain))[0][0]
        var[i] = (s - k.dot(Kinv).dot(k.T))[0][0]
    return mu, var
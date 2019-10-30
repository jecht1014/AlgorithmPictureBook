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
def rbf(x1, x2, params, coordinate=None):
    [tau,sigma,eta] = params
    if coordinate is None or coordinate[0] == coordinate[1]:
        return np.exp(tau) * np.exp(-np.power(x2 - x1, 2) / np.exp(sigma)) + np.exp(eta)*np.eye(x2.shape[0])
    else:
        return np.exp(tau) * np.exp(-np.power(x2 - x1, 2) / np.exp(sigma))

def kernel_partial_differentiation(x1, x2, params, kernel, h=0.000001):
    a, b, c = np.log(theta1), np.log(theta2), np.log(theta3)
    #hena = (rbf(x1, x2, theta1=np.exp(a+h), theta2=np.exp(b), theta3=np.exp(c)) - rbf(x1, x2, theta1=np.exp(a+h), theta2=np.exp(b), theta3=np.exp(c))) / h
    #henb = (rbf(x1, x2, theta1=np.exp(a), theta2=np.exp(b+h), theta3=np.exp(c)) - rbf(x1, x2, theta1=np.exp(a+h), theta2=np.exp(b), theta3=np.exp(c))) / h
    #henc = (rbf(x1, x2, theta1=np.exp(a), theta2=np.exp(b), theta3=np.exp(c+h)) - rbf(x1, x2, theta1=np.exp(a+h), theta2=np.exp(b), theta3=np.exp(c))) / h
    return (hena, henb, henc)

# 線形カーネル関数
def linear_kernel(x1, x2, params, coordinate=None):
    [tau] = params
    if coordinate is None or coordinate[0] == coordinate[1]:
        return x1*x2 + np.exp(tau)*np.eye(x2.shape[0])
    else:
        return x1*x2

# 指数カーネル関数
def exponential_kernel(x1, x2, params):
    [tau,sigma] = params
    if coordinate is None or coordinate[0] == coordinate[1]:
        return np.exp(-np.abs(x1 - x2) / np.exp(tau)) + np.exp(sigma)*np.eye(x2.shape[0])
    else
        return np.exp(-np.abs(x1 - x2) / np.exp(tau))

# 周期カーネル
def periodic_kernel(x1, x2, params):
    [tau,sigma,eta] = params
    if coordinate is None or coordinate[0] == coordinate[1]:
        return np.exp(np.exp(tau) * np.cos(np.abs(x1-x2) / np.exp(sigma))) + np.exp(eta)*np.eye(x2.shape[0])
    else:
        return np.exp(np.exp(tau) * np.cos(np.abs(x1-x2) / np.exp(sigma)))

# Matern3
def matern3(x1, x2, params):
    [tau,sigma] = params
    if coordinate is None or coordinate[0] == coordinate[1]:
        return (1 + np.sqrt(3) * np.abs(x1 - x2) / np.exp(tau)) * np.exp(-np.sqrt(3) * np.abs(x1 - x2) / np.exp(tau)) + np.exp(sigma)*np.eye(x2.shape[0])
    else:
        return (1 + np.sqrt(3) * np.abs(x1 - x2) / np.exp(tau)) * np.exp(-np.sqrt(3) * np.abs(x1 - x2) / np.exp(tau))

# Matern5
def matern5(x1, x2, params):
    [tau,sigma] = params
    if coordinate is None or coordinate[0] == coordinate[1]:
        return (1 + np.sqrt(5) * np.abs(x1 - x2) / np.exp(tau) + 5 * np.power(x1-x2, 2) / (3 * np.power(x1-x2, 2))) * np.exp(-np.sqrt(5) * np.abs(x1-x2) / np.exp(tau)) + np.exp(sigma)*np.eye(x2.shape[0])
    else:
        return (1 + np.sqrt(5) * np.abs(x1 - x2) / np.exp(tau) + 5 * np.power(x1-x2, 2) / (3 * np.power(x1-x2, 2))) * np.exp(-np.sqrt(5) * np.abs(x1-x2) / np.exp(tau))

# カーネルで共分散行列の作製
def make_k(x, params, kernel):
    x2 = np.tile(x.T, (x.shape[0], 1))
    k = kernel(x, x2, params)
    return k

# ガウス過程回帰(ハイパーパラメータ最適化なし)
def gaussian_process(xtrain, xtest, ytrain, ytest, params, kernel=rbf):
    K = make_k(xtrain, params, kernel)
    k = np.zeros((1, ytrain.shape[0]))
    Kinv = np.linalg.inv(K)

    mu = np.zeros(ytest.shape[0])
    var = np.zeros(ytest.shape[0])
    for i in range(ytest.shape[0]):
        for j in range(ytrain.shape[0]):
            k[0][j] = kernel(xtrain[j], xtest[i], params, (i, j))
        s = kernel(xtest[i], xtest[i], params)
        mu[i] = (k.dot(Kinv).dot(ytrain))[0][0]
        var[i] = (s - k.dot(Kinv).dot(k.T))[0][0]
    return mu, var

# ガウス過程回帰(ハイパーパラメータ最適化あり)
def gaussian_process_(xtrain, ytrain, sigma2=0.1, kernel=rbf):
    K = make_k(xtrain, sigma2, kernel)
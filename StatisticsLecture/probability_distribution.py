import numpy as np
import matplotlib.pyplot as plt
from math import factorial

class Discrete:
    def __init__(self, value: np.ndarray, probability: np.ndarray):
        self.value = value
        self.probability = probability

    # 期待値(平均)
    def expectation(self):
        return np.sum(self.value*self.probability)

    # 分散
    def var(self):
        return np.sum(np.power(self.value-self.expectation(), 2)*self.probability)
    
    # 確率関数のプロット
    def plot_probability_function(self, save_path):
        plt.bar(self.value, self.probability, width=0.1, color='blue', tick_label=self.value, align="center")
        plt.savefig(save_path)
        plt.close()

    # 分布関数のプロット
    def plot_distribution_function(self, save_path):
        v = 0
        plt.xlim(self.value[0]-1, self.value[-1]+1)
        plt.plot([self.value[0]-1,self.value[0]], [0, 0], color='blue')
        for i in range(len(self.value)-1):
            v += self.probability[i]
            plt.plot(self.value[i:i+2], [v, v], color='blue')
        plt.plot([self.value[-1], self.value[-1]+1], [1, 1], color='blue')
        plt.savefig(save_path)
        plt.close()

class Continuous:
    def __init__(self, function, x_range: tuple, x=None):
        self.function = function
        self.x_range = x_range
        self.x = x

    # 期待値(平均)
    def expectation(self, num=int(1e4), use_x_flag: bool=False):
        if not use_x_flag:
            x = np.linspace(self.x_range[0], self.x_range[1], num)
        else:
            x = self.x
        y = self.function(x) * x
        e = 0
        for i in range(x.shape[0]-1):
            e += (x[i+1]-x[i]) * (y[i]+y[i+1]) / 2
        return e

    # 2乗平均
    def expectation2(self, num=int(1e4), use_x_flag: bool=False):
        if not use_x_flag:
            x = np.linspace(self.x_range[0], self.x_range[1], num)
        else:
            x = self.x
        y = self.function(x) * x * x
        e = 0
        for i in range(x.shape[0]-1):
            e += (x[i+1]-x[i]) * (y[i]+y[i+1]) / 2
        return e

    # 分散
    def var(self, use_x_flag: bool=False):
        return self.expectation2(use_x_flag=use_x_flag)-np.power(self.expectation(use_x_flag=use_x_flag), 2)

    # z-変換
    def z_transform(self, use_x_flag: bool=False, num=int(1e4)):
        if use_x_flag:
            return (self.x - self.expectation(use_x_flag=use_x_flag)) / np.sqrt(self.var(use_x_flag=use_x_flag))
        else:
            return (np.linspace(self.x_range[0], self.x_range[1], num) - self.expectation(use_x_flag=use_x_flag)) / np.sqrt(self.var(use_x_flag=use_x_flag))

    # 確率関数のプロット
    def plot_probability_function(self, save_path, num=int(1e4)):
        x = np.linspace(self.x_range[0], self.x_range[1], num)
        plt.plot(x, self.function(x))
        plt.savefig(save_path)
        plt.close()

    # 分布関数のプロット
    def plot_distribution_function(self, save_path, num=int(1e4)):
        x = np.linspace(self.x_range[0], self.x_range[1], num)
        y = self.function(x)
        dy = np.array([0])
        for i in range(num-1):
            dy = np.append(dy, dy[-1]+(x[i+1]-x[i]) * (y[i]+y[i+1]) / 2)
        plt.xlim(self.x_range[0], self.x_range[1])
        plt.plot(x, dy)
        plt.savefig(save_path)
        plt.close()

# ベルヌーイ分布
def bernoulli(p):
    return (np.array([0, 1]), np.array([1-p, p]))

# 2項分布
def binomial(n=18, p=0.1667):
    def comb(n, r):
        return factorial(n) / factorial(r) / factorial(n - r)
    x = np.arange(0, n+1)
    probability = np.array([comb(n, x_i)*(p**x_i)*(1-p)**(n-x_i) for x_i in x])
    return (x, probability)

# ポアソン分布
def poisson(lamb=3):
    x = np.array([0, 1])
    p = np.array([np.exp(-lamb)*np.power(lamb, 0)/factorial(0), np.exp(-lamb)*np.power(lamb, 1)/factorial(1)])
    while(p[-2] < p[-1] or (p[-2] >= p[-1] and p[-1] > 1e-6)):
        x = np.append(x, x[-1]+1)
        p = np.append(p, np.exp(-lamb)*np.power(lamb, x[-1])/factorial(x[-1]))
    return (x, p)

# 一様乱数
def uniform(x: np.ndarray, alfa=0, beta=2):
    p = np.where((x >= alfa) & (x <= beta), 1/(beta-alfa), 0)
    return p

# 指数分布
def exponential(x: np.ndarray, lamb=2):
    return (lamb * np.exp(-lamb*x))

# 正規分布
def norm(x: np.ndarray, mu=0, sigma2=1):
    return (1/np.sqrt(2*np.pi*sigma2)) * np.exp(-np.power(x-mu, 2)/(2*sigma2))

value, probability = bernoulli(0.8)
discrete = Discrete(value, probability)
discrete.plot_probability_function('image/bernoulli_probability.png')
discrete.plot_distribution_function('image/bernoulli_distribution.png')

continuous = Continuous(norm, (-5, 5))
continuous.plot_probability_function('image/norm_probability.png')
continuous.plot_distribution_function('image/norm_distribution.png')
print(continuous.expectation())
print(continuous.var())

value, probability = poisson()
discrete = Discrete(value, probability)
discrete.plot_probability_function('image/poisson_probability.png')
discrete.plot_distribution_function('image/poisson_distribution.png')

continuous = Continuous(exponential, (0, 4))
continuous.plot_probability_function('image/exp_probability.png')
continuous.plot_distribution_function('image/exp_distribution.png')
print(continuous.expectation())
print(continuous.var())

continuous = Continuous(uniform, (0, 2), np.array([0, 1, 2]))
z = continuous.z_transform(use_x_flag=False)
continuous.plot_probability_function('image/uni_probability.png')
continuous.plot_distribution_function('image/uni_distribution.png')
print(continuous.expectation())
print(continuous.var())
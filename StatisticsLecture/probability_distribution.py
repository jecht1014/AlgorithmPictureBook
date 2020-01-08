import numpy as np
import matplotlib.pyplot as plt

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
        plt.bar(self.value, self.probability, width=0.01, color='blue', tick_label=self.value, align="center")
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
    def __init__(self, function, x_range: tuple):
        self.function = function
        self.x_range = x_range

    # 期待値(平均)
    def expectation(self, num=10000):
        x = np.linspace(self.x_range[0], self.x_range[1], num)
        y = self.function(x) * x
        e = 0
        for i in range(num-1):
            e += (x[i+1]-x[i]) * (y[i]+y[i+1]) / 2
        return e
    # 2乗平均
    def expectation2(self, num=10000):
        x = np.linspace(self.x_range[0], self.x_range[1], num)
        y = self.function(x) * x * x
        e = 0
        for i in range(num-1):
            e += (x[i+1]-x[i]) * (y[i]+y[i+1]) / 2
        return e

    # 分散
    def var(self):
        return self.expectation2()-np.power(self.expectation(), 2)

    # 確率関数のプロット
    def plot_probability_function(self, save_path, num=10000):
        x = np.linspace(self.x_range[0], self.x_range[1], num)
        plt.plot(x, self.function(x))
        plt.savefig(save_path)
        plt.close()

    # 分布関数のプロット
    def plot_distribution_function(self, save_path, num=10000):
        x = np.linspace(self.x_range[0], self.x_range[1], num)
        y = self.function(x)
        dy = np.array([0])
        for i in range(num-1):
            dy = np.append(dy, dy[-1]+(x[i+1]-x[i]) * (y[i]+y[i+1]) / 2)
        plt.xlim(self.x_range[0], self.x_range[1])
        plt.plot(x, dy)
        plt.savefig(save_path)
        plt.close()

def bernoulli(p):
    return (np.array([0, 1]), np.array([1-p, p]))

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
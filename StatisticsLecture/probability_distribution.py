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

def bernoulli(p):
    return (np.array([0, 1]), np.array([1-p, p]))

value, probability = bernoulli(0.8)
discrete = Discrete(value, probability)
discrete.plot_probability_function('image/bernoulli_probability.png')
discrete.plot_distribution_function('image/bernoulli_distribution.png')
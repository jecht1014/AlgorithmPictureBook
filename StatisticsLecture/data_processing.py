import numpy as np
import csv
import matplotlib.pyplot as plt

# 粗データの処理
class DataProcessing:
    def __init__(self, data: np.ndarray):
        # 粗データから中央値を出力
        def calc_median(data):
            if (data.shape[0] % 2 == 1):
                return data[int(data.shape[0]/2)]
            else:
                return (data[int(data.shape[0]/2-1)]+data[int(data.shape[0]/2)])/2
        
        self.data = data # 粗データ
        self.data.sort()
        
        # 四分位点
        self.quartile = [0]*3
        self.quartile[1] = calc_median(self.data)
        if (data.shape[0] % 2 == 1):
            self.quartile[0] = calc_median(self.data[:int(data.shape[0]/2)])
            self.quartile[2] = calc_median(self.data[int(data.shape[0]/2)+1:])
        else:
            self.quartile[0] = calc_median(self.data[:int(data.shape[0]/2)])
            self.quartile[2] = calc_median(self.data[int(data.shape[0]/2):])

    # 粗データから度数分布を出力
    # sturgesをTrueにするとすとスタージェスの定理に従って階級数を決定
    def coarse2frequency(self, sturges: bool=True, width: int=None):
        if (sturges):
            width = np.ceil((self.data[-1]-self.data[0])/int(np.ceil(1+np.log2(self.data.shape[0]))))
        left = int(self.data[0])
        right = left+width

        class_value = np.array([])
        frequency = np.array([])
        for _ in range(int(np.ceil((self.data[-1]-self.data[0])/width))):
            class_value = np.append(class_value, (left+right)/2)
            # class_value = np.append(class_value, left)
            frequency = np.append(frequency, np.sum((left < self.data) & (self.data <= right)))
            left += width
            right += width

        return (class_value, frequency)

    def avg(self):
        return np.average(self.data)

    # 分散
    def var(self):
        print(self.avg())
        return np.sum(np.power(self.data-self.avg(), 2)) / self.data.shape[0]

    # 不偏分散
    def u_var(self):
        return np.sum(np.power(self.data-self.avg(), 2)) / (self.data.shape[0]-1)

    # 平均偏差
    def md(self):
        return np.sum(np.abs(self.data-self.avg())) / self.data.shape[0]

# 度数分布の処理
class FrequencyDistribution:
    def __init__(self, class_value: np.ndarray, frequency: np.ndarray):
        self.class_value = class_value
        self.frequency = frequency
        self.data_num = np.sum(self.frequency)

    # 平均
    def avg(self):
        return np.sum(self.class_value*self.frequency)/self.data_num

    # 分散
    def var(self):
        return np.sum(np.power(self.class_value, 2)*self.frequency)/self.data_num - self.avg() ** 2

    # 不偏分散
    def u_var(self):
        return np.sum(np.power(self.class_value, 2)*self.frequency)/(self.data_num-1) - self.avg() ** 2
    
    # 最頻値
    def mode(self):
        arg_freq = self.frequency.argmax()
        return self.class_value[arg_freq]
    
    # 度数分布表を保存
    def plot_frequency(self, save_path):
        plt.bar(self.class_value, self.frequency, width=self.class_value[1]-self.class_value[0], color='blue', edgecolor='cyan', tick_label=self.class_value, align="center")
        plt.savefig(save_path)
        plt.close()

data = []
with open('data/newborn_weight.csv') as f:
    reader = csv.reader(f)
    [data.append(int(row[0])) for row in reader]
data = np.array(data)
dosu = DataProcessing(data)
class_value, freq = dosu.coarse2frequency()
#print(dosu.quartile)
print(dosu.avg())
print(dosu.var())
print(dosu.u_var())
print(dosu.md())

freq_class = FrequencyDistribution(class_value, freq)
print(freq_class.avg())
print(freq_class.var())
freq_class.plot_frequency('image/frequency_distribution.png')
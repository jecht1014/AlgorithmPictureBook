import numpy as np
import csv
import matplotlib.pyplot as plt

class FrequencyDistribution:
    def __init__(self, data: np.ndarray):
        # 粗データから中央値を出力
        def calc_median(data):
            if (data.shape[0] % 2 == 1):
                return data[int(data.shape[0]/2)]
            else:
                return (data[int(data.shape[0]/2-1)]+data[int(data.shape[0]/2)])/2
        
        # 粗データが与えられたとき
        if (data.ndim == 1):
            self.data = data # 粗データ
            self.data.sort()
            self.avg = self.data.mean() # 平均
            
            # 四分位点
            self.quartile = [0]*3
            self.quartile[1] = calc_median(self.data)
            if (data.shape[0] % 2 == 1):
                self.quartile[0] = calc_median(self.data[:int(data.shape[0]/2)])
                self.quartile[2] = calc_median(self.data[int(data.shape[0]/2)+1:])
            else:
                self.quartile[0] = calc_median(self.data[:int(data.shape[0]/2)])
                self.quartile[2] = calc_median(self.data[int(data.shape[0]/2):])

            self.mode = None # 最頻値

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

        # 最頻値の格納
        arg_freq = frequency.argmax()
        self.mode = class_value[arg_freq]

        return (class_value, frequency)
    
    # 度数分布表を保存
    def plot_frequency(self, class_value, frequency, save_path):
        plt.bar(class_value, frequency, width=class_value[1]-class_value[0], color='blue', edgecolor='cyan', tick_label=class_value, align="center")
        plt.savefig(save_path)

data = []
with open('data/newborn_weight.csv') as f:
    reader = csv.reader(f)
    [data.append(int(row[0])) for row in reader]
data = np.array(data)
dosu = FrequencyDistribution(data)
dosu_bunpu = dosu.coarse2frequency()
print(dosu.quartile)
print(dosu.mode)
dosu.plot_frequency(dosu_bunpu[0], dosu_bunpu[1], 'image/frequency_distribution.png')
import numpy as np
import csv
import matplotlib.pyplot as plt

class FrequencyDistribution:
    def __init__(self, data: np.ndarray):
        self.data = data
        self.data.sort()

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
dosu.plot_frequency(dosu_bunpu[0], dosu_bunpu[1], 'image/frequency_distribution.png')
import pandas as pd
import matplotlib.pyplot as plt

class FrequencyTable:
    """
    度数分布表
    """
    def __init__(self, row_data: list, class_interval: int, num_of_class: int, min_class_mark: int):
        """
        Parameters
        ----------
        row_data : list
            粗データ
        class_interval : int
            階級幅
        num_of_class : int
            階級数
        min_class_mark : int
            最小の階級値
        """
        self.row_data = row_data
        self.class_interval = class_interval
        self.num_of_class = num_of_class
        self.max_row_data = max(row_data)
        self.min_row_data = min(row_data)
        self.length = len(row_data)

        data = {
            'number': [i for i in range(1, self.num_of_class+1)],
            'class_mark': [min_class_mark+class_interval*i for i in range(0, self.num_of_class)],
            'frequency': [0]*self.num_of_class
        }

        # 度数の計算
        for row in self.row_data:
            for i in range(self.num_of_class):
                if (data['class_mark'][i]-class_interval/2 < float(row) <= data['class_mark'][i]+class_interval/2):
                    data['frequency'][i] += 1
                    break

        self.frequency_table = pd.DataFrame(data).set_index('number')

        #下限値と上限値を追加
        self.frequency_table['lower_limit'] = self.frequency_table['class_mark']-class_interval/2
        self.frequency_table['upper_limit'] = self.frequency_table['class_mark']+class_interval/2

        # 累積度数の追加
        self.frequency_table['cumulative_frequency'] = self.frequency_table['frequency'].cumsum()

        # 比率の追加
        self.frequency_table['ratio'] = self.frequency_table['frequency']/self.length

        # 累積比率の追加
        self.frequency_table['cumulative_ratio'] = self.frequency_table['cumulative_frequency']/self.length
    
    def range(self) -> float:
        """
        データの範囲を返す関数

        Returns
        -------
        float
            データの範囲
        """
        return self.max_row_data-self.min_row_data

    def plot_histogram(self) -> None:
        """
        ヒストグラムを描画する関数
        """
        self.frequency_table.plot.bar("class_mark", "frequency", width=1)
        plt.show()
    
    def plot_frequency_polygon(self) -> None:
        """
        度数多角形を描画する関数
        """
        self.frequency_table.plot("class_mark", "frequency")
        plt.show()
    
    def plot_cumulative_ratio_chart(self) -> None:
        """
        累積比率図を描画する関数
        """
        self.frequency_table.plot("upper_limit", "cumulative_ratio")
        plt.show()

    def average(self) -> float:
        """
        平均の計算を行う関数

        Returns
        -------
        float
            平均
        """
        return (self.frequency_table['class_mark']*self.frequency_table['frequency']).sum()/self.length
    
    def median(self) -> float:
        """
        中央値の計算を行う関数

        Returns
        -------
        float
            中央値
        """
        v = self.frequency_table.query('cumulative_ratio > 0.5')[0:1]
        return (v['lower_limit'] + self.class_interval * (self.length/2.0 - (v['cumulative_frequency']-v['frequency'])) / v['frequency']).iloc[-1]

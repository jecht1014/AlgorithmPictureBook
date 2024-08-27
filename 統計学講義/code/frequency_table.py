import pandas as pd

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
    
    def range(self) -> float:
        """
        データの範囲を返す関数

        Returns
        -------
        float
            データの範囲
        """
        return self.max_row_data-self.min_row_data
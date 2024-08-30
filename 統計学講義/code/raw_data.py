import pandas as pd

class RawData:
    """
    粗データを扱うクラス
    """
    
    def __init__(self, raw_data: list):
        self.raw_data = raw_data
        self.length = len(raw_data)
    
    def mean(self) -> float:
        """
        平均の計算を行う関数

        Returns
        -------
        float
            平均
        """
        return sum(self.raw_data)/self.length
    
    def median(self) -> float:
        """
        中央値の計算を行う関数

        Returns
        -------
        float
            中央値
        """
        sorted_raw_data = sorted(self.raw_data)
        if self.length % 2 == 0:
            return (sorted_raw_data[self.length//2] + sorted_raw_data[self.length//2-1])/2
        else:
            return sorted_raw_data[self.length//2]
        
    def variance(self) -> float:
        """
        分散の計算を行う関数

        Returns
        -------
        float
            分散
        """
        
        return sum([(i-self.mean())**2 for i in self.raw_data])/(self.length)
    
    def unbiased_variance(self) -> float:
        """
        不偏分散の計算を行う関数

        Returns
        -------
        float
            分散
        """
        
        return sum([(i-self.mean())**2 for i in self.raw_data])/(self.length-1)

    def standard_deviation(self) -> float:
        """
        標準偏差の計算を行う関数

        Returns
        -------
        float
            標準偏差
        """
        
        return self.variance()**0.5

    def unbiased_standard_deviation(self) -> float:
        """
        不偏標準偏差の計算を行う関数

        Returns
        -------
        float
            標準偏差
        """
        
        return self.unbiased_variance()**0.5
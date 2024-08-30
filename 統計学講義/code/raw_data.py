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
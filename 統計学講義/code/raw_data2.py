import raw_data

class RawData2:
    """
    2次元の粗データを扱うクラス
    """
    
    def __init__(self, raw_data: list[int|float]):
        """
        コンストラクタ

        Parameters
        ----------
        raw_data : list[int|float]
            粗データ
        """
        self.raw_data = raw_data
        self.length = len(raw_data)

    def covariance(self) -> float:
        """
        共分散の計算を行う関数

        Returns
        -------
        float
            共分散
        """
        
        x_mean = raw_data.RawData([raw[0] for raw in self.raw_data]).mean()
        y_mean = raw_data.RawData([raw[1] for raw in self.raw_data]).mean()
        return sum([(raw[0]-x_mean)*(raw[1]-y_mean) for raw in self.raw_data])/(self.length)

    def correlation_coefficient(self) -> float:
        """
        相関係数の計算を行う関数

        Returns
        -------
        float
            相関係数
        """
        x_standard_deviation = raw_data.RawData([raw[0] for raw in self.raw_data]).standard_deviation()
        y_standard_deviation = raw_data.RawData([raw[1] for raw in self.raw_data]).standard_deviation()
        return self.covariance()/(x_standard_deviation*y_standard_deviation)

import math
import matplotlib.pyplot as plt
import numpy as np

class Parabola():
    """放物線の各属性値や関数を持つ
    Attributes
    ----------
    forcus : float
        焦点
    semiLatusRectum : float
        半直弦
    y : list
        プロット用のy座標のリスト
    x : list
        プロット用のx座標のリスト
    """
    def __init__(self, forcus:float):
        """コンストラクタ

        Parameters
        ----------
        forcus : float
            焦点
        """
        self.forcus = forcus
        self.semiLatusRectum = 2 * forcus
        self.y = []
        self.x = []
    
    def calc(self, x:float, isPositiveInteger:bool=True):
        """x座標からy座標を導出

        Parameters
        ----------
        x : float
            x座標
        isPositiveInteger : bool, optional
            導出されたy座標が正かどうか, by default True

        Returns
        -------
        float
            y座標
        """
        y = math.sqrt(4 * self.forcus * x)
        return y if (isPositiveInteger) else -y
    
    def calcRange(self, start=0.0, stop=5.0, step=0.01):
        """x座標が[start, stop)で階差が0.01の時のy座標を計算する

        Parameters
        ----------
        start : float, optional
            x座標のレンジの小さいほう, by default 0
        stop : float, optional
            x座標のレンジの大きいほう, by default 5
        step : float, optional
            startとstopの間をいくつずつカウントアップするか, by default 0.01
        """
        for i in np.arange(stop, start, -step):
            self.x.append(i)
            self.y.append(self.calc(x=i))
        for i in np.arange(start, stop, step):
            self.x.append(i)
            self.y.append(self.calc(x=i, isPositiveInteger=False))
    
    def plot(self, hasForcus=False, hasDirectrix=False, hasSemiLatusRectum=False):
        """放物線をプロットする

        Parameters
        ----------
        hasForcus : bool, optional
            焦点をプロットするか, by default False
        hasDirectrix : bool, optional
            準線をプロットするか, by default False
        hasSemiLatusRectum : bool, optional
            半直弦をプロットするか, by default False
        """
        # x軸とy軸の表示
        plt.axhline(0, linewidth=1, color="gray")
        plt.axvline(0, linewidth=1, color="gray")

        # x軸とy軸のスケーリングが同じになるように変更
        plt.gca().set_aspect('equal', adjustable='box')

        # 放物線の表示
        plt.plot(self.x, self.y, label="parabola")

        # 焦点の表示
        if (hasForcus):
            plt.plot(self.forcus, 0, marker='.', color="green", label="forcus")

        # 準線の表示
        if (hasDirectrix):
            plt.axvline(-self.forcus, color="green", label="directrix")
        
        plt.plot([self.forcus, self.forcus], [self.forcus, self.semiLatusRectum], label="semi-latus rectum")

        plt.plot()
        plt.legend()
        plt.show()

class Ellipse():
    """楕円の各属性値や関数を持つ
    Attributes
    ----------
    majorAxis : float
        長軸
    semiMajorAxis : float
        半長軸
    minorAxis : float
        短軸
    semiMinorAxis : float
        半短軸
    forcus : float
        焦点
    eccentricity : float
        離心率
    semiLatusRectum : float
        半直弦
    y : list
        プロット用のy座標のリスト
    x : list
        プロット用のx座標のリスト
    """

    def __init__(self, majorAxis:float, forcus:float=None, minorAxis:float=None):
        """コンストラクタ
        majorAxisは必須で、forcusとminorAxisはどちらかが必須(両方の利用は×)

        Parameters
        ----------
        majorAxis : float
            長軸
        forcus : float, optional
            焦点, by default None
        minorAxis : float, optional
            短軸, by default None

        Raises
        ------
        ValueError
            引数が不正な場合のエラー
        """
        self.majorAxis = majorAxis
        self.semiMajorAxis = majorAxis / 2
        if (forcus is not None and minorAxis is None):
            self.forcus = forcus
            self.semiMinorAxis = math.sqrt(self.semiMajorAxis**2 - self.forcus**2)
            self.minorAxis = 2 * self.semiMinorAxis
        elif (minorAxis is not None and forcus is None):
            self.minorAxis = minorAxis
            self.semiMinorAxis = minorAxis / 2
            self.forcus = math.sqrt(self.semiMajorAxis**2 - self.semiMinorAxis**2)
        else:
            raise ValueError("minorAxisとforcusのどちらかに値をセットしてください")
        self.eccentricity = self.forcus / self.semiMajorAxis
        self.semiLatusRectum = self.semiMajorAxis * (1 - self.eccentricity**2)
        self.y = []
        self.x = []
        
    def calc(self, x:float, isPositiveInteger=True) -> float:
        """与えられたx座標からy座標を計算する

        Parameters
        ----------
        x : float
            x座標
        isPositiveInteger : bool, optional
            y座標が正か, by default True

        Returns
        -------
        float
            y座標
        """
        y = math.sqrt(self.semiMinorAxis**2 * (1-(x**2/self.semiMajorAxis**2)))
        return y if (isPositiveInteger) else -y

    def calcRange(self, step = 0.01):
        """x軸をstep区切りで計算して楕円の計算を行う

        Parameters
        ----------
        step : float, optional
            x軸をいくつごとに区切って求めるか, by default 0.01
        """
        for i in np.arange(-self.semiMajorAxis, self.semiMajorAxis, step):
            self.x.append(i)
            self.y.append(self.calc(x=i))
        for i in np.arange(self.semiMajorAxis, -(self.semiMajorAxis+step), -step):
            self.x.append(i)
            self.y.append(self.calc(x=i, isPositiveInteger=False))
    
    def plot(self, hasForcus:bool=False):
        # x軸とy軸の表示
        plt.axhline(0, linewidth=1, color="gray")
        plt.axvline(0, linewidth=1, color="gray")

        # x軸とy軸のスケーリングが同じになるように変更
        plt.gca().set_aspect('equal', adjustable='box')

        # 楕円のプロット
        plt.plot(self.x, self.y, label="ellipse")

        # 焦点のプロット
        if (hasForcus):
            plt.scatter([-1 * self.forcus, self.forcus], [0, 0], label="forcus")

        plt.plot()
        plt.legend()
        plt.show()

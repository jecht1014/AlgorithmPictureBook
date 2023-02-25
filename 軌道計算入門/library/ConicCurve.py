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

class Hyperbola():
    """双曲線の各属性値や関数を持つ
    """
    def __init__(self, vertex: float, coVertex: float=None, focus: float=None) -> None:
        """コンストラクタ
        vertexは必須で、focusとcoVertexはどちらかが必須(両方の利用は✖️)

        Parameters
        ----------
        vertex : float
            原点と双曲線の距離
        coVertex : float, optional
            vertexと漸近線の距離, by default None
        focus : float, optional
            焦点, by default None

        Raises
        ------
        ValueError
            引数が不正な場合のエラー
        """
        self.vertex = vertex
        # 交軸
        self.transverseAxis = 2 * self.vertex
        if (focus is not None and coVertex is None):
            self.focus = focus
            self.coVertex = math.sqrt(self.focus**2-self.vertex**2)
        elif (coVertex is not None and focus is None):
            self.coVertex = coVertex
            self.focus = math.sqrt(coVertex**2 - vertex**2)
        else:
            raise ValueError("coVertexとfocusのどちらかに値をセットしてください")

        # vertexと双曲線の距離
        self.conjugateAxis = 2 * self.coVertex
        # 離心率
        self.eccentricity = self.focus / self.vertex
        # 半直弦
        self.semiLatusRectum = self.vertex * (self.eccentricity**2 - 1)
        # プロット用のx軸座標のリスト
        self.x = []
        # プロット用のy軸座標のリスト
        self.y = []
    
    def calc(self, x: float, isPositiveInteger=True) -> float:
        """与えられたx座標からy座標を計算する

        Parameters
        ----------
        x : float
            x座標
        isPositiveInteger : bool, optional
            y軸が正か, by default True

        Returns
        -------
        float
            y座標
        """
        y = (self.coVertex / self.vertex) * math.sqrt(x**2 - self.vertex**2)
        return y if (isPositiveInteger) else -y
    
    def calcRange(self, stop=5.0, step=0.01):
        """x座標が[self.vertex, stop]で階差が0.01の時のy座標を計算する

        Parameters
        ----------
        stop : float, optional
            x座標の連木の大きい方, by default 5.0
        step : float, optional
            vertexとstopの間をいくつずつカウントアップするか, by default 0.01
        """
        # x > 0の時の双曲線
        for i in np.arange(stop, self.vertex, -step):
            self.x.append(i)
            self.y.append(self.calc(x=i))
        for i in np.arange(self.vertex, stop, step):
            self.x.append(i)
            self.y.append(self.calc(x=i, isPositiveInteger=False))

        # 描画しないようにNoneの追加
        self.x.append(None)
        self.y.append(None)

        # x < 0の時の双曲線
        for i in np.arange(-stop, -self.vertex, step):
            self.x.append(i)
            self.y.append(self.calc(x=i))
        for i in np.arange(-self.vertex, -stop, -step):
            self.x.append(i)
            self.y.append(self.calc(x=i, isPositiveInteger=False))

    def calcAsymptote(self, x: float, isPositiveSlope=True) -> float:
        """x座標から漸近線のy座標を計算する

        Parameters
        ----------
        x : float
            x座標
        isPositiveSlope : bool, optional
            漸近線の傾きが正か, by default True

        Returns
        -------
        float
            y座標
        """
        slope = self.coVertex/self.vertex
        return abs(slope) * x if (isPositiveSlope) else -abs(slope) * x

    def calcAsymptoteToPlot(self):
        """プロットするために漸近線を計算する

        Returns
        -------
        tuple
            x座標のリストとy座標のリストのタプル
        """
        # self.xからNoneを取り除いたリストを取得
        listOfXWithNoneRemoved = list(filter(lambda x: x is not None, self.x))
        minX, maxX = min(listOfXWithNoneRemoved), max(listOfXWithNoneRemoved)
        x = [minX, maxX, None, minX, maxX]
        y = [self.calcAsymptote(x[0]), self.calcAsymptote(x[1]), None, self.calcAsymptote(x[3], False), self.calcAsymptote(x[4], False)]
        return (x, y)
    
    def plot(self, hasFocus: bool=False, hasAsymptote: bool=False) -> None:
        """双曲線をプロット

        Parameters
        ----------
        hasFocus : bool, optional
            焦点をプロットするか, by default False
        hasAsymptote : bool, optional
            漸近線をプロットするか, by default False
        """
        # x軸とy軸の表示
        plt.axhline(0, linewidth=1, color="gray")
        plt.axvline(0, linewidth=1, color="gray")

        # 双曲線のプロット
        plt.plot(self.x, self.y, label="Hyperbola")

        # 焦点のプロット
        if (hasFocus):
            plt.scatter([-1 * self.focus, self.focus], [0, 0], label="focus")
        
        # 漸近線のプロット
        if (hasAsymptote):
            (asymptoteX, asymptoteY) = self.calcAsymptoteToPlot()
            plt.plot(asymptoteX, asymptoteY, label="asymptote")

        plt.grid(True)
        plt.legend()
        plt.show()
from __future__ import annotations


class Matrix:
    """
    行列クラス
    """

    matrix: list[list[int | float]]

    def __init__(self, matrix: list[list[float]]) -> None:
        """コンストラクタ

        Parameters
        ----------
        matrix : list[float]
            行列
        """
        self.matrix = matrix

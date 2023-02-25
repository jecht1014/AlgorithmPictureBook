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

    def equal(self, matrix: Matrix) -> bool:
        """行列が等しいか

        Parameters
        ----------
        matrix : Matrix
            比較対象の行列

        Returns
        -------
        bool
            行列が等しいか
        """
        return self.matrix == matrix.matrix

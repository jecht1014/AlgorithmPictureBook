from __future__ import annotations
import copy


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

    def __eq__(self, other: Matrix):
        """等しいの定義

        Parameters
        ----------
        other : Matrix
            比較対象の行列

        Returns
        -------
        _type_
            _description_
        """
        return self.matrix == other.matrix

    def zero_matrix(rows: int, columns: int) -> Matrix:
        """零行列を作成

        Parameters
        ----------
        rows : int
            行数
        columns : int
            列数

        Returns
        -------
        Matrix
            rows行, columns列の0行列
        """
        return Matrix([[0 for _ in range(rows)] for _ in range(columns)])

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

    def to_string(self) -> str:
        """行列を文字列で表示

        Returns
        -------
        str
            行列
        """
        [print(row) for row in self.matrix]

matrix = Matrix.zero_matrix(2, 3)
print(matrix.to_string())
print(Matrix([[0, 0], [0, 0], [0, 0]]).to_string())

print(matrix.matrix)
print(Matrix([[0, 0], [0, 0], [0, 0]]).matrix)

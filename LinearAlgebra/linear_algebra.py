from __future__ import annotations
import copy


class Matrix:
    """
    行列クラス
    """

    matrix: list[list[int | float]]

    def __init__(self, matrix: list[list[int | float]]) -> None:
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

    def create_zero_matrix(rows: int, columns: int) -> Matrix:
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

    def plus(self, target_matrix: Matrix) -> Matrix:
        if not (
            self.rows() == target_matrix.rows()
            and self.columns() == target_matrix.columns()
        ):
            raise ValueError("行と列の数が等しくありません")

        # 結果を入れる行列の初期化
        result: Matrix = Matrix.create_zero_matrix(self.rows(), self.columns())
        for row in range(self.rows()):
            for column in range(self.columns()):
                result.matrix[row][column] = (
                    self.matrix[row][column] + target_matrix.matrix[row][column]
                )
        return result

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

    def rows(self) -> int:
        """行数

        Returns
        -------
        int
            行数
        """
        return len(self.matrix)

    def columns(self) -> int:
        """列数

        Returns
        -------
        int
            列数
        """
        return len(self.matrix[0])

    def is_square_matrix(self) -> bool:
        """正方行列(列数 == 行数)かどうか

        Returns
        -------
        bool
            正方行列か
        """
        return self.rows() == self.columns()

    def to_square_matrix(self) -> SquareMatrix:
        """正方行列クラスに変換

        Returns
        -------
        SquareMatrix
            正方行列クラス
        """
        return SquareMatrix(self.matrix)


class SquareMatrix(Matrix):
    def __init__(self, matrix: list[list[int | float]]) -> None:
        """コンストラクタ

        Parameters
        ----------
        matrix : list[list[float]]
            正方行列のリスト

        Raises
        ------
        TypeError
            正方行列以外が渡された時の例外
        """
        super().__init__(matrix)
        if not self.is_square_matrix():
            raise ValueError(
                "対象の行列が正方行列ではありません: rows=", self.rows(), ", columns=", self.columns()
            )

    def create_identity_matrix(size: int) -> SquareMatrix:
        """単位行列を作成

        Parameters
        ----------
        size : int
            _description_

        Returns
        -------
        SquareMatrix
            _description_
        """
        matrix: Matrix = Matrix.create_zero_matrix(size, size)
        for i in range(size):
            matrix.matrix[i][i] = 1
        return matrix.to_square_matrix()

    def diagonal_element(self) -> list[int | float]:
        """対角成分

        Returns
        -------
        list[int | float]
            対角成分のリスト
        """
        return [self.matrix[i][i] for i in range(self.rows())]

    def is_upper_triangular_matrix(self) -> bool:
        """上三角行列かどうか

        Returns
        -------
        bool
            上三角行列か
        """
        for row in range(self.rows()):
            for column in range(self.columns()):
                if row > column and self.matrix[row][column] != 0:
                    return False
        return True

    def is_lower_triangular_matrix(self) -> bool:
        """下三角行列かどうか

        Returns
        -------
        bool
            下三角行列かどうか
        """
        for row in range(self.rows()):
            for column in range(self.columns()):
                if row < column and self.matrix[row][column] != 0:
                    return False
        return True

    def is_diagronal_matrix(self) -> bool:
        """下三角行列かどうか

        Returns
        -------
        bool
            下三角行列かどうか
        """
        for row in range(self.rows()):
            for column in range(self.columns()):
                if row != column and self.matrix[row][column] != 0:
                    return False
        return True

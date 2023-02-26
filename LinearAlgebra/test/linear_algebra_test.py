import unittest
import os
import sys

sys.path.append(os.path.abspath(".."))
from linear_algebra import Matrix, SquareMatrix


# equalのtest
class MatrixTestCase(unittest.TestCase):
    matrix_list = [[0, 1], [2, 3]]
    not_equal_matrix_list = [[0, 1, 2], [3, 4, 5]]

    matrix = Matrix(matrix_list)
    equal_matrix = Matrix(matrix_list)
    not_equal_matrix = Matrix(not_equal_matrix_list)

    def test_equal(self):
        """同じ行列を与えた時にequal関数がtrueを返すかテスト"""
        self.assertTrue(self.matrix.equal(self.equal_matrix))

    def test_not_equal(self):
        """異なる行列を与えた時にequal関数がfalseを返すかテスト"""
        self.assertFalse(self.matrix.equal(self.not_equal_matrix))

    zero_matrix = Matrix([[0, 0], [0, 0], [0, 0]])
    rows = 2
    columns = 3

    def test_create_zero_matrix(self):
        """想定した零行列が作成されるかテスト"""
        self.assertEqual(
            self.zero_matrix, Matrix.create_zero_matrix(self.rows, self.columns)
        )

    square_matrix = Matrix([[0, 1], [2, 3]])
    not_square_matrix = Matrix([[0, 1], [2, 3], [4, 5]])

    def test_is_square_matrix(self):
        """正方行列を与えた時trueを返すかテスト"""
        self.assertTrue(self.square_matrix.is_square_matrix())

    def test_is_not_square_matrix(self):
        """正方行列以外を与えた時falseを返すかテスト"""
        self.assertFalse(self.not_square_matrix.is_square_matrix())

    def test_plus(self):
        """正常に足し算が行われるかテスト"""
        matrix = Matrix([[0, 1], [2, 3]])
        target_matrix = Matrix([[1, 3], [5, 7]])
        expected_matrix = Matrix([[1, 4], [7, 10]])
        self.assertEqual(matrix.plus(target_matrix), expected_matrix)

    def test_plus_value_exception(self):
        """行数か列数が一致しない時に例外がスローされるかテスト"""
        matrix = Matrix([[0, 1], [2, 3]])
        target_matrix = Matrix([[1, 3], [5, 7], [9, 11]])
        with self.assertRaises(ValueError):
            matrix.plus(target_matrix)

    def test_minus(self):
        """正常に引き算が行われるかテスト"""
        matrix = Matrix([[0, 1], [2, 3]])
        target_matrix = Matrix([[1, 3], [5, 7]])
        expected_matrix = Matrix([[-1, -2], [-3, -4]])
        self.assertEqual(matrix.minus(target_matrix), expected_matrix)

    def test_minus_value_exception(self):
        """行数か列数が一致しない時に例外がスローされるかテスト"""
        matrix = Matrix([[0, 1], [2, 3]])
        target_matrix = Matrix([[1, 3], [5, 7], [9, 11]])
        with self.assertRaises(ValueError):
            matrix.minus(target_matrix)

    def test_minus(self):
        """正常にスカラー積が行われるかテスト"""
        matrix = Matrix([[0, 1], [2, 3]])
        num = 2
        expected_matrix = Matrix([[0, 2], [4, 6]])
        self.assertEqual(matrix.scalar_multiply_by(num), expected_matrix)


# 正方行列クラスのテスト
class SquareMatrixTestCase(unittest.TestCase):
    square_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).to_square_matrix()
    diagonal_element = [1, 5, 9]

    def test_diagonal_element(self):
        """対角成分が正しいかのテスト"""
        self.assertEqual(self.square_matrix.diagonal_element(), self.diagonal_element)

    upper_triangular_matrix = Matrix([[1, 2], [0, 4]]).to_square_matrix()
    lower_triangular_matrix = Matrix([[1, 0], [3, 4]]).to_square_matrix()
    diagonal_matrix = Matrix([[1, 0], [0, 4]]).to_square_matrix()

    def test_is_upper_triangular_matrix(self):
        """上三角行列の時にtrueを返すかのテスト"""
        self.assertTrue(self.upper_triangular_matrix.is_upper_triangular_matrix())

    def test_is_not_upper_triangular_matrix(self):
        """上三角行列ではない行列を与えた時にfalseを返すかテスト"""
        self.assertFalse(self.lower_triangular_matrix.is_upper_triangular_matrix())

    def test_is_lower_triangular_matrix(self):
        """下三角行列の時にtrueを返すかのテスト"""
        self.assertTrue(self.lower_triangular_matrix.is_lower_triangular_matrix())

    def test_is_not_lower_triangular_matrix(self):
        """下三角行列ではない行列を与えた時にfalseを返すかテスト"""
        self.assertFalse(self.upper_triangular_matrix.is_lower_triangular_matrix())

    def test_is_diagronal_matrix(self):
        """対角行列の時にtrueを返すかのテスト"""
        self.assertTrue(self.diagonal_matrix.is_diagronal_matrix())

    def test_is_not_diagronal_matrix(self):
        """対角行列ではない行列を与えた時にfalseを返すかテスト"""
        self.assertTrue(self.diagonal_matrix.is_diagronal_matrix())

    identity_matrix = SquareMatrix.create_identity_matrix(3)
    expected_identity_matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    def test_create_identity_matrix(self):
        """単位行列が作成されるか"""
        self.assertEqual(self.identity_matrix, self.expected_identity_matrix)

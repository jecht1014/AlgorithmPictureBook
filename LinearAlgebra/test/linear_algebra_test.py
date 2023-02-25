import unittest
import os
import sys

sys.path.append(os.path.abspath(".."))
from linear_algebra import Matrix, SquareMatrix


# equalのtest
class EqualTestCase(unittest.TestCase):
    matrix_list = [[0, 1], [2, 3]]
    not_equal_matrix_list = [[0, 1, 2], [3, 4, 5]]

    matrix = Matrix(matrix_list)
    equal_matrix = Matrix(matrix_list)
    not_equal_matrix = Matrix(not_equal_matrix_list)

    def test_equal(self):
        self.assertTrue(self.matrix.equal(self.equal_matrix))

    def test_not_equal(self):
        self.assertFalse(self.matrix.equal(self.not_equal_matrix))


# zero_matrixのtest
class ZeroMatrixTestCase(unittest.TestCase):
    zero_matrix = Matrix([[0, 0], [0, 0], [0, 0]])
    rows = 2
    columns = 3

    def test_zero_matrix(self):
        self.assertEqual(self.zero_matrix, Matrix.zero_matrix(self.rows, self.columns))


# is_square_matrixのテスト
class IsSquareMatrixTestCase(unittest.TestCase):
    square_matrix = Matrix([[0, 1], [2, 3]])
    not_square_matrix = Matrix([[0, 1], [2, 3], [4, 5]])

    def test_is_square_matrix(self):
        self.assertTrue(self.square_matrix.is_square_matrix())

    def test_is_not_square_matrix(self):
        self.assertFalse(self.not_square_matrix.is_square_matrix())


# 正方行列クラス
# diagonal_elementのテスト
class DiagonalElementTestCase(unittest.TestCase):
    square_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).to_square_matrix()
    diagonal_element = [1, 5, 9]

    def test_diagonal_element(self):
        self.assertEqual(self.square_matrix.diagonal_element(), self.diagonal_element)

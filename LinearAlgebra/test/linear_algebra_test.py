import unittest
import os
import sys

sys.path.append(os.path.abspath(".."))
from linear_algebra import Matrix

# equalのtest
matrix_list = [[0, 1], [2, 3]]
not_equal_matrix_list = [[0, 1, 2], [3, 4, 5]]

matrix = Matrix(matrix_list)
equal_matrix = Matrix(matrix_list)
not_equal_matrix = Matrix(not_equal_matrix_list)


class EqualTestCase(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(matrix.equal(equal_matrix))

    def test_not_equal(self):
        self.assertFalse(matrix.equal(not_equal_matrix))

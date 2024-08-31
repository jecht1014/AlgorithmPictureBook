import unittest
import csv
from pathlib import Path

import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
import raw_data2

class TestRawData2(unittest.TestCase):
    """
    raw_data2.pyのテスト
    """

    def setUp(self) -> None:
        """
        テスト用のcsvファイルを事前に読み込む
        """
        parent = Path(__file__).resolve().parent
        row_data = []

        # テスト用のcsvファイルの読み込み
        with open(parent.joinpath('../sample_data/StatData02_1.csv')) as f:
            reader = csv.reader(f)
            row_data = [row for row in reader][1:]
            row_data = [[float(row[1]), float(row[2])] for row in row_data]

        self.raw_data2 = raw_data2.RawData2(row_data)

    def test_convariance(self):
        """
        共分散のテスト
        """
        self.assertAlmostEqual(self.raw_data2.covariance(), 424.24, places=2)

    def test_correlation_coefficient(self):
        """
        相関係数のテスト
        """
        self.assertAlmostEqual(self.raw_data2.correlation_coefficient(), 0.783, places=2)

unittest.main()
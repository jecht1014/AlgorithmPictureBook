import unittest
import csv
from pathlib import Path

import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
import frequency_table

class TestFrequencyTable(unittest.TestCase):
    """
    frequency_table.pyのテスト
    """

    def setUp(self) -> None:
        """
        テスト用のcsvファイルを事前に読み込む
        """
        parent = Path(__file__).resolve().parent
        row_data = []

        # テスト用のcsvファイルの読み込み
        with open(parent.joinpath('../sample_data/StatData01_1.csv')) as f:
            reader = csv.reader(f)
            row_data = [row[0] for row in reader][1:]
            row_data = [int(row) for row in row_data]

        self.frequency_table = frequency_table.FrequencyTable(row_data, 200, 11, 2200)

    def test_mean(self):
        """
        平均のテスト
        """
        self.assertEqual(self.frequency_table.mean(), 3154)

    def test_median(self):
        """
        中央値のテスト
        """
        self.assertEqual(self.frequency_table.median(), 3150)

    def test_mode(self):
        """
        最頻値のテスト
        """
        self.assertAlmostEqual(self.frequency_table.mode(), 3170.59, places=2)

    def test_variance(self):
        """
        分散のテスト
        """
        self.assertEqual(self.frequency_table.variance(), 159084)
    
    def test_unbiased_variance(self):
        """
        不偏分散のテスト
        """
        self.assertEqual(self.frequency_table.unbiased_variance(), 159084*(100/99.0))

    def test_standard_deviation(self):
        """
        標準偏差のテスト
        """
        self.assertAlmostEqual(self.frequency_table.standard_deviation(), 398.85, places=2)
    
    def test_unbiased_standard_deviation(self):
        """
        不偏標準偏差のテスト
        """
        self.assertAlmostEqual(self.frequency_table.unbiased_standard_deviation(), 398.85*(100/99.0)**0.5, places=2)
    
    def test_mean_deviation(self):
        """
        平均偏差のテスト
        """
        self.assertEqual(self.frequency_table.mean_deviation(), 311.52)
    
    def test_quantile(self):
        """
        四分位点のテスト
        """
        self.assertAlmostEqual(self.frequency_table.quantile(1), 2886.67, places=2)
        self.assertAlmostEqual(self.frequency_table.quantile(2), 3150, places=2)
        self.assertAlmostEqual(self.frequency_table.quantile(3), 3407.69, places=2)

        # 1, 2, 3以外の値を入力するとエラーになる
        with self.assertRaises(ValueError):
            self.frequency_table.quantile(4)
    
    def test_interquartile_range(self):
        """
        四分位範囲のテスト
        """
        self.assertAlmostEqual(self.frequency_table.interquartile_range(), 521.03, places=2)

unittest.main()
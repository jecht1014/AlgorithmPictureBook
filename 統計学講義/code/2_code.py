import csv
from pathlib import Path
import frequency_table
import matplotlib.pyplot as plt

parent = Path(__file__).resolve().parent
row_data = []
with open(parent.joinpath('sample_data/StatData01_1.csv')) as f:
    reader = csv.reader(f)
    row_data = [row[0] for row in reader][1:]
    row_data = [int(row) for row in row_data]

frequency_table = frequency_table.FrequencyTable(row_data, 200, 11, 2200)
frequency_table.plot_histogram()
frequency_table.plot_frequency_polygon()
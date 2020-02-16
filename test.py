import csv

from datetime import datetime

import matplotlib.pyplot as plt 

filename = 'data/eindhoven_2019_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)
    header_row = next(reader)
    print(header_row)
    header_row = next(reader)
    print(header_row)
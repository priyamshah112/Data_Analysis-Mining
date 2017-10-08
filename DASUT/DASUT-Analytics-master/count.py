import pandas as pd
import csv

row_count = sum(1 for row in csv.reader( open('C:/Python 3.6/DATA ANALYSIS/DASUT/DASUT-Analytics-master/user_data.csv') ) )
print(row_count)

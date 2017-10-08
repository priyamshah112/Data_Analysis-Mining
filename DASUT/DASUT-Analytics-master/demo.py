import pandas as pd
import csv
a=pd.read_csv('C:/Python 3.6/DATA ANALYSIS/DASUT/DASUT-Analytics-master/user_data.csv')
#print(a.head(7))
print(a.loc[0:6,:])
b=a.loc[1,'Unnamed: 1']
print(b)

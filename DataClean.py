import pandas as pd

data = pd.read_csv('car_data.csv')

print(data.isnull().sum())

data.dropna(inplace=True) 

print(data.head())

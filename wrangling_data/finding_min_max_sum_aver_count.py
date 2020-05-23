import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

print("Max: ", dataframe['Age'].max())
print("Min: ", dataframe['Age'].min())
print("Mean: ", dataframe['Age'].mean())
print("Sum: ", dataframe['Age'].sum())
print("Count: ", dataframe['Age'].count())
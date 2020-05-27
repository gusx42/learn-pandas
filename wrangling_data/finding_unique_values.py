import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#Select unique values
print(dataframe['Sex'].unique())

# count unique values from column
print(dataframe['Sex'].value_counts())

# Show value_counts
print(dataframe['PClass'].value_counts())

# Show number of unique values
print(dataframe['PClass'].nunique())
import pandas as pd

url = 'https://tinyurl.com//titanic-csv'

dataframe = pd.read_csv(url)

#select top two rows where column 'sex' is 'female'
print(dataframe[dataframe['Sex'] == 'female'].head(100))

#select from all register where sex is 'female' and 'age'>=65
print(dataframe[(dataframe['Sex'] == 'female') & (dataframe['Age'] >= 50)])
import pandas as pd

url = 'https://tinyurl.com//titanic-csv'

dataframe = pd.read_csv(url)

#select first row
print(dataframe.iloc[0])


#select first column 4 rows
print(dataframe.iloc[0:4])

#select first column 4 rows
print(dataframe.iloc[:10])

#Create  a index for column name
dataframe = dataframe.set_index(dataframe['Name'])

#find name
print(dataframe.loc['Allen, Miss Elisabeth Walton'])



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#sample of 5 first list
print(dataframe.head)

#all dataframe
print(dataframe)

#number of rows and collumns
print(dataframe.shape)

#statistics of dataframe
print(dataframe.describe())

#sample of list 
print(dataframe.tail(200))



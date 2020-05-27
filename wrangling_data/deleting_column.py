import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

#load data
dataframe = pd.read_csv(url)

#delete column
dataframe.drop('Age', axis=1).head(2)

dataframe.drop(['Age', 'Sex'], axis=1).head(2)


dataframe.drop(dataframe.columns[1], axis=1).head(2)
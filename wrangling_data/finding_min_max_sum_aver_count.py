import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#Finding the Minimum, Maximum, Sum, Average, and Count
print("maximum: ", dataframe['Age'].max())
print("minimum: ", dataframe['Age'].min())
print("average: ", dataframe['Age'].mean())
print("sum: ", dataframe['Age'].sum())
print("count: ", dataframe['Age'].count())


#variance (var), standard deviation (std), kurtosis (kurt), skewness (skew), standard error of the mean (sem), mode (mode), median (median)
print("variance: ", dataframe['Age'].var())
print("standard deviation: ", dataframe['Age'].std())
print("kurtosis: ", dataframe['Age'].kurt())
print("skewness: ", dataframe['Age'].skew())
print("standard error of the mean : ", dataframe['Age'].sem())
print("mode : ", dataframe['Age'].mode())
print("median : ", dataframe['Age'].median())

print("count by column from dataframe: ", dataframe.count())
import pandas as pd
import numpy as np

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#find value where age is null
print(dataframe[dataframe['Age'].isnull()].head(2))

#replace male from NAN
dataframe['Sex'] = dataframe['Sex'].replace('male', np.nan)

print(dataframe)

#replace missing values
dataframe = pd.read_csv(url, na_values=[np.nan, 'NONE', -999])

print(dataframe)
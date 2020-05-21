import pandas as pd
import collections

url = 'http://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

# Rename column and return the first two lines
print(dataframe.rename(columns={'PClass': 'Passanger Class'}).head(2))


# Rename more than one column
print(dataframe.rename(
    columns={'PClass': 'Passanger Class', 'Sex': 'Gender'}).head(2))


# Create a dict with all colums
columns_names = collections.defaultdict(str) 

# Append all values with 'new'
for name in dataframe.columns:
    print(name)
    columns_names[name] = f'{name}-new'

print(columns_names)
# Replace coluns
print(dataframe.rename(columns=columns_names).head(2))

git remote add origin https://github.com/gusxpander/learn-pandas



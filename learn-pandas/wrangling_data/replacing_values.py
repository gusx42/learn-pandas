import pandas as pd

url = 'https://tinyurl.com//titanic-csv'

dataframe = pd.read_csv(url)

# Repalce 'female' for 'Woman' and show
print(dataframe['Sex'].replace('female','Woman').head(2))

# Replace 'female' for 'Woman' and 'male' for 'Man' 
print(dataframe['Sex'].replace(['female','Woman'],['male','Man']).head(5))

# Get all ocurrences like 1 and replace for "One" and show 2 lines
print(dataframe.replace(1, "One").head(50))

# Repalce using regex, replace and show 2 lines
print(dataframe.replace(r"1st", "First", regex=True).head(2))


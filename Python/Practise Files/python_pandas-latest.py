import pandas as pd

# Load Files Into a DataFrame

df = pd.read_csv('E:/testdata/apple_products.csv')
print(df)
print(df.to_string())

df = pd.read_csv('E:/testdata/apple_products.csv')
af = pd.DataFrame(df, index = ["Product Name","Sale Price","Discount Percentage"])
print(af)
print(af.to_string())
# max_rows
print(df.head()) 
print(df.head(15))
#using tail()
print(df.tail())     # Will display only last 5 rows from bottom by default
print(df.tail(15))  # last 15 rows from bottom including header

print(df.isnull()) 
print(df.isna())
print(df.to_string())

  # To get the information of datasets

# Data cleaning Remove empty cells / rows from a data set
df1 = pd.read_csv('E:/testdata/apple_products.csv')
df1.info()
newdf = df1.dropna(inplace = True)      # will return new data set and no change in original
print(newdf)

df = pd.read_csv('D:/prac/detail.csv')
new_df = df.dropna(inplace = False) # will change in original data set
print(new_df.to_string())
new_df.to_csv("E:/testdata/data1.csv")


# Inserting new values in empty cells in original dataset

df1 = pd.read_csv('E:/testdata/apple_products.csv')
df1.fillna(555, inplace = True)
print(df1.to_string())
df1.to_csv("E:/testdata/newdata8.csv")

# Replaces all empty cells in the whole Data Frame.
df1 = pd.read_csv('E:/testdata/apple_products.csv')
df1["Sale Price"].fillna(777, inplace = True)

print(df1["Sale Price"].to_string())
df1.to_csv("E:/testdata/newdata9.csv")
import pandas as pd
# Replce empty cell by using Mean(), Median(), Mode()
df1 = pd.read_csv('E:/testdata/apple_products.csv')
x = df1["Sale Price"].mean()         #calculate the respective values for a specified column:
x
#df1["Sale Price"].fillna(x, inplace = True)
df1.fillna(x, inplace = True)
print(df1.to_string())
df1.to_csv("E:/testdata/newdata11.csv")
# Replce empty cell by using Median()
df = pd.read_csv('C:/Users/cdac/Desktop/ytube.csv')
x = df["commentCount"].median()          #calculate the respective values for a specified column:
df["commentCount"].fillna(x, inplace = True)
print(df["commentCount"].to_string())                                        

# Replce empty cell by using  Mode()         
df = pd.read_csv('D:/prac/ytube.csv')
x = df["commentCount"].mode()          #calculate the respective values for a specified column:
df["commentCount"].fillna(x, inplace = True)
print(df["commentCount"].to_string())

# Cleaning wrong data
df = pd.read_csv('D:/prac/ytube.csv')
df['pub_date'] = pd.to_datetime(df['pub_date'])  
print(df["pub_date"].to_string())
# Removing cells containing wrong data
df = pd.read_csv('D:/prac/ytube.csv')
df.dropna(subset=['pub_date'], inplace = True)
print(df["pub_date"].to_string())
# Fixing wrong data
df = pd.read_csv('D:/prac/ytube.csv')
df.loc[7, 'pub_date'] = '07-08-2023'
print(df["pub_date"].to_string())

# To check whether any duplicate rows exist in dataset
df = pd.read_csv('D:/prac/ytube.csv')
print(df.duplicated())
df.drop_duplicates(inplace = True)
print(df)

# Corelation in python
df.corr()
print(df.to_string())

# Matplotlib to visulize the result on screen import matplotlib.pyplot as plt library

import matplotlib.pyplot as plt 
df = pd.read_csv('C:/Users/cdac/Desktop/loan_data.csv')
df.plot()
df.plot(kind = 'hist', x = 'Duration', y = 'Calories')
plt.show()



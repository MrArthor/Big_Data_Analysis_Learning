import pandas as pd    # Pandas libraray 

mydataset = {'cars': ["BMW", "Volvo", "Ford"],'passings': [3, 7, 2]}
myvar = pd.DataFrame(mydataset)
print(myvar)

# checking the version of pandas library

print(pd.__version__)

# Pandas series
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# Lables in Pndas

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar[0])    # will use index and print value 1

# creating labels in pandas 

a = [5, 10, 22]
myvar = pd.Series(a, index = ["Car", "Bus", "Motorcycle"])
print(myvar)
print(myvar["Bus"])   # access an item by using to the label.

# Key/Value base object in creation of series

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

#  Create a Series using dataset index

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day3"])
print(myvar)

# Creation of Dataframe using two datasets

data = {"calories": [420, 380, 390],"duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)

# 
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)      #load data into a DataFrame object:
#print(df)  
#print(df.loc[0])             # will reperesent single first row
print(df.loc[[0, 1]])      # will reperesent three rows 0,1,2
 
# addix index in dataframe as per requirement

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
# Load Files Into a DataFrame

df = pd.read_csv('C:/Users/cdac/Desktop/loan_data.csv')
af = pd.DataFrame(df, index = ["Loan_paid","Loan_not_paid","Defaulter"])
print(af)
print(af.to_string())
  # max_rows
print(pd.options.display.max_rows)

# Reading JSON file using Pandas library

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 

# Analyzing the data using head() method

df = pd.read_csv('C:/Users/cdac/Desktop/loan_data.csv')

#print(df.head(5)) 
#print(df.head(15))
#using tail()
#print(df.tail())     # Will display only last 5 rows from bottom by default
print(df.tail(15))  # last 15 rows from bottom including header

print(df.info())   # To get the information of datasets

# Data cleaning Remove empty cells / rows from a data set
df = pd.read_csv('C:/Users/cdac/Desktop/loan_data.csv')
new_df = df.dropna()     # will return new data set and no change in original
newdf = df.dropna(inplace = True) # will change in original data set
print(new_df.to_string())

# Inserting new values in empty cells in original dataset

df = pd.read_csv('C:/Users/cdac/Desktop/loan_data.csv')
df.fillna(25, inplace = True)
print(df.to_string())

# Replaces all empty cells in the whole Data Frame.
df = pd.read_csv('C:/Users/cdac/Desktop/loan_data.csv')
df["installment"].fillna(777, inplace = True)
print(df["installment"].to_string())

# Replce empty cell by using Mean(), Median(), Mode()
df = pd.read_csv('C:/Users/cdac/Desktop/ytube.csv')
x = df["commentCount"].mean()           #calculate the respective values for a specified column:
df["commentCount"].fillna(x, inplace = True)
print(df["commentCount"].to_string())
# Replce empty cell by using Median()
df = pd.read_csv('C:/Users/cdac/Desktop/ytube.csv')
x = df["commentCount"].median()          #calculate the respective values for a specified column:
df["commentCount"].fillna(x, inplace = True)
print(df["commentCount"].to_string())                                        

# Replce empty cell by using  Mode()         
df = pd.read_csv('C:/Users/cdac/Desktop/ytube.csv')
x = df["commentCount"].mode()          #calculate the respective values for a specified column:
df["commentCount"].fillna(x, inplace = True)
print(df["commentCount"].to_string())
# Cleaning wrong data
df = pd.read_csv('C:/Users/cdac/Desktop/ytube.csv')
df['pub_date'] = pd.to_datetime(df['pub_date'])  
print(df["pub_date"].to_string())
# Removing cells containing wrong data
df = pd.read_csv('C:/Users/cdac/Desktop/ytube.csv')
df.dropna(subset=['pub_date'], inplace = True)
print(df["pub_date"].to_string())
# Fixing wrong data
df = pd.read_csv('C:/Users/cdac/Desktop/ytube.csv')
df.loc[7, 'pub_date'] = 45
print(df["pub_date"].to_string())

# To check whether any duplicate rows exist in dataset
df = pd.read_csv('C:/Users/cdac/Desktop/ytube.csv')
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



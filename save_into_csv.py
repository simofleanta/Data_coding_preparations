#create a python program to read csv without csv module

import pandas as pd
#open file
df=pd.read_csv("GitHub_data.csv")
#show the type of the df
print(type(df))
#print it just the first 3 rows
print(df.head(3))
#convert pandas df to a numpy array
array=df.to_numpy()
print(array)

#open file
df=pd.read_csv("Inflation_forecast.csv")
#show the type of the df
print(type(df))
#print it just the first 3 rows
print(df.head(3))
#convert pandas df to a numpy array
array=df.to_numpy()
print(array)

#saving into csv for further processing

c=df.to_csv






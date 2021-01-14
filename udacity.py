import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import numpy as np
import plotly
import statistics
import plotly.express as px
import stats
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import plotly.express as px
import datetime

"""In my Udacity Data Science Challenge, I was supposed to practice Python and create some data visuals using pandas data frames, with data. The aim of 
the exercise was to go through basic data types, data frames and juggling with the data so obtain a small data analysis on random data

So this ex will go through:
opening file
checking data types and making sense of the data
date timeseries parsing
one or 2 carts 
subplots 
"""

#open file
u=pd.read_csv('udacity.csv')
print(u.columns)
udacity=DataFrame(u.head(60))
print(udacity.head(60))

#check dtypes
print(udacity.dtypes)
# if we hve null values 
print(udacity.isnull)
#shape of data
print(udacity.shape)
#data description
print(udacity.describe())

#parse index
udacity['year']=pd.to_datetime(udacity['year'], infer_datetime_format=True)
indexeddf=udacity.set_index(['year'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=udacity['year']=pd.to_datetime(udacity['year'], format='%d-%m-%y')

Day=udacity['year'].dt.day_name()
Month=udacity['year'].dt.month_name()
Year=udacity['year'].dt.year

#subsetting 
udacity['Year']=udacity['year'].dt.year
udacity['Month']=udacity['year'].dt.month_name()
udacity['Day']=udacity['year'].dt.day_name()


#Analyzing data using Python  Seaborn charts

#subplot 
f,axes = plt.subplots(1,2, figsize=(15, 10))
fig1=sns.violinplot(x=udacity["Products"], y=udacity["Profit"], palette="summer",ax=axes[0])
fig2=sns.boxplot(udacity.Place, udacity.Profit, palette='viridis',hue_order=[True,False],ax=axes[1])
plt.show()

#scatter subplot
f,axes = plt.subplots(1,2, figsize=(15, 10))
A=sns.scatterplot(udacity.Out_px, udacity.Profit, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0])

B=sns.scatterplot(udacity.Margin, udacity.Profit, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[1])

plt.show()

#correlation map
sns.heatmap(udacity.corr(), annot=True, cmap='Blues', linewidth=1,vmin=-1,vmax=1, yticklabels=True,xticklabels=True)
plt.show()






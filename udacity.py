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

u=pd.read_csv('udacity.csv')
print(u.columns)
udacity=DataFrame(u.head(60))
print(udacity.head(60))

#check dtypes
print(udacity.dtypes)
# if we hve null values 
print(udacity.isnull)
print(udacity.shape)
print(udacity.describe())


udacity['year']=pd.to_datetime(udacity['year'], infer_datetime_format=True)
indexeddf=udacity.set_index(['year'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=udacity['year']=pd.to_datetime(udacity['year'], format='%d-%m-%y')

Day=udacity['year'].dt.day_name()
print(Day)

Month=udacity['year'].dt.month_name()
print(Month)

Year=udacity['year'].dt.year
print(Year)

#subsetting 
udacity['Year']=udacity['year'].dt.year
udacity['Month']=udacity['year'].dt.month_name()
udacity['Day']=udacity['year'].dt.day_name()
print(udacity.head(31))

#operate




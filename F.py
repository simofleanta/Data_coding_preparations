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


c=pd.read_csv('Energy_consumption.csv')
print(c.columns)
df_c=DataFrame(c.head(31))
print(df_c.head(31))

df_c['Date']=pd.to_datetime(df_c['Date'], infer_datetime_format=True)
indexeddf=df_c.set_index(['Date'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'

x=df_c['Date']=pd.to_datetime(df_c['Date'], format='%y-%m-%d')

Day=df_c['Date'].dt.day_name()
print(Day)

Month=df_c['Date'].dt.month_name()
print(Month)

Year=df_c['Date'].dt.year
print(Year)

#subsetting 
df_c['Year']=df_c['Date'].dt.year
df_c['Month']=df_c['Date'].dt.month_name()
df_c['Day']=df_c['Date'].dt.day_name()
print(df_c.head(31))

#calculate consumtion hours before app
df_c['consumtion_hours_before_app']=df_c.KwH_Before_App*df_c.Active_Hours
df_c['consumtion_hours_After_app']=df_c.KwH_After_App*df_c.Active_Hours

#print the whole consumption data
print(df_c)

#print desired columns to prepare for visuals 
print(df_c.columns)

data=df_c[['Day','Weather','Temperature_Celsius','KwH_Before_App','KwH_After_App','Active_Hours','consumtion_hours_before_app','consumtion_hours_After_app']].copy()
print(data)




















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

#My client wants to see if it is worth monitoring electrical energy in order to optimze costs and consumption behaviour.
#I was given a data sample for one month in order to extract insights. 
#opened data
#processed time series
#calculated before and after consumption
#extracted insights into seaborn darshboards

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

#plotting consumption patterns before app 
f,axes = plt.subplots(2,2, figsize=(15,30))
K0=sns.scatterplot(data.KwH_Before_App, data.Active_Hours, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0,0])

k1=sns.stripplot(x='Day', y='Active_Hours',jitter=0.25, marker='*',alpha=0.6, size=10, linewidth=1, palette="Blues", data=data, \
    ax=axes[0,1])

k2=sns.boxplot(data.Weather, data.KwH_Before_App, palette='Blues',hue_order=[True,False],ax=axes[1,0])

k3=sns.scatterplot(data.Temperature_Celsius, data.consumtion_hours_before_app, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues', ax=axes[1,1])

plt.show()

#the more hours the more active the larger consumption
#at the begining of the week and end of the week, there are more ative hours and therefore consumption
#the worst the weather the higher kwH consumption.


#In order to understand the trends in the dashboard, I have added a separate correlation map
sns.heatmap(data.corr(), annot=True, cmap='Blues', linewidth=1,vmin=-1,vmax=1, yticklabels=True,xticklabels=False)
plt.show()

#analizing trends after app 

f,axes = plt.subplots(2,2, figsize=(15,30))
K0=sns.scatterplot(data.KwH_After_App, data.Active_Hours, s=100, edgecolor='black', alpha=0.5,\
     palette='viridis',ax=axes[0,0])

x1=sns.stripplot(x='Day', y='KwH_After_App',jitter=0.25, marker='*',alpha=0.6, size=10, linewidth=1, palette="viridis", data=data, \
    ax=axes[0,1])

x2=sns.boxplot(data.Weather, data.KwH_After_App, palette='viridis',hue_order=[True,False],ax=axes[1,0])

x3=sns.scatterplot(data.Temperature_Celsius, data.consumtion_hours_After_app, s=100, edgecolor='black', alpha=0.5,\
     palette='summer', ax=axes[1,1])

plt.show()

#trends remain as above but because numbers are smaller they are more evident. 
#the more hours the more active the larger consumption
#at the begining of the week and end of the week, there are more ative hours and therefore consumption
#the worst the weather the higher kwH consumption.


#short benchmark of KwH between situations before and after app

f,axes = plt.subplots(1,2, figsize=(15, 10))
A=sns.scatterplot(data.Active_Hours, data.consumtion_hours_before_app, s=100, edgecolor='black', alpha=0.5,\
     palette='husl',ax=axes[0])

B=sns.scatterplot(data.Active_Hours, data.consumtion_hours_After_app, s=100, edgecolor='black', alpha=0.5,\
     palette='husl',ax=axes[1])

plt.show()

#calculate how much Kwh was saved (as%)
data['Saved_KwH']=(data.consumtion_hours_before_app-data.consumtion_hours_After_app)/100
print(data)

#Conclusions

#not big differences spottted, most propbably because consumption behaviour was much the same and data was only processed for 1 mth.
#Nevertheless differences show clear benefits of using monitoring app in order to optimize costs and behaviour.
#the short answer is yes use the monitoring app as on a longer term it may be even more usefull. 




















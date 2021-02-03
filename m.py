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

m=pd.read_csv('Actual.csv')
print(m.columns)
m=DataFrame(m.head(10))
print(m.head(10))

#types_of_data
print(m.dtypes)

#parse index
m['Date']=pd.to_datetime(m['Date'], infer_datetime_format=True)
indexeddf=m.set_index(['Date'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=m['Date']=pd.to_datetime(m['Date'], format='%m-%d-%y')

Day=m['Date'].dt.day
Month=m['Date'].dt.month_name()
Year=m['Date'].dt.year

#subsetting 
m['Year']=m['Date'].dt.year
m['Month']=m['Date'].dt.month_name()
m['Day']=m['Date'].dt.day
print(m)

#indexing per month 

#Month_index per month 'M' 
Month_index=indexeddf.resample('M')
print(Month_index)

# see sum for both months jan and feb
Sum_M_index=indexeddf.resample('M').sum()
print(Sum_M_index)

#subplot 
f,axes = plt.subplots(1,2, figsize=(15, 10))
fig1=sns.violinplot(x=m["Month"], y=m["Actual_Revenue"], palette="viridis",ax=axes[0]).set_title("Monthly Actual Revenue")
fig2=sns.boxplot(m.Marketing_Channel, m.Actual_Revenue, palette='Blues',hue_order='Month',ax=axes[1]).set_title("Actual Revenue per Channel")
plt.show()

###############

#Trends

#scatter subplot to see monthly trend and daily trend
f,axes = plt.subplots(1,2, figsize=(15, 10))
A=sns.scatterplot(m.Month, m.Actual_Revenue, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0]).set_title("Monthy Revenue scatter chart")

B=sns.scatterplot(m.Day, m.Actual_Revenue, s=100, edgecolor='black', alpha=0.5,\
     palette='viridis',ax=axes[1]).set_title("Daily Revenue trend chart")
plt.show()


#m to csv fro forecast in power bi
df=m.to_csv('forecast.csv')

#forecast_multiply aurorevenue by number of months or days 
















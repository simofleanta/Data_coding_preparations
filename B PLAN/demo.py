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
import time 


c=pd.read_csv('bread basket.csv')
print(c.columns)
df=DataFrame(c.head(100))
print(df.head(100))

#c=df.select_dtypes(object)
#print(c)

a=df.shape
print(a)
b=df.dtypes
print(b)

#groupings
x=df.groupby(['period_day','Item'])[['Transaction']]
#print(x.mean())
y=df.groupby(['Item','weekday_weekend','period_day'])[['Transaction']]
#print(y.mean())

#Aggregate
operations=['mean','sum','min','max']
a=df.groupby(['Item','period_day'], as_index=False)[['Transaction']].agg(operations)
print(a.reset_index())

#sort asc
data=df['Item'].value_counts().sort_values(ascending=False).head(10)
print(data)

#plot preferred products

fig, ax=plt.subplots(figsize=(6,4))
df['Item'].value_counts().sort_values(ascending=False).head(10).plot(kind='bar')
plt.ylabel('Transaction')
plt.xlabel('Item')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Preferred products')
#plt.show()

#when is the bakery doing the most business during the day?

b=df.groupby('period_day')['Item'].count().sort_values(ascending=False)
print(b)

fig, ax=plt.subplots(figsize=(5,4))
sns.set_style('darkgrid')
df.groupby('period_day')['Item'].count().sort_values().plot(kind='bar')
plt.ylabel('Transaction')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Business during the day')

#graphing the groupings
df.groupby('date_time')['Item'].count().plot(kind='bar')
plt.ylabel('Transaction')
plt.title('Business during the past time')

#pivoting
data2=df.pivot_table(index='period_day',columns='Item', aggfunc={'Item':'count'}).fillna(0)
data2['Max']=data2.idxmax(axis=1)
print(data2)




















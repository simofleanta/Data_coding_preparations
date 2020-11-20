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


c=pd.read_csv('bike_business_plan.csv')
#print(c.columns)
df=DataFrame(c.head(700))
print(df.head(700))

sns.violinplot(x=df["Item"], y=df["Price"], palette="Blues")
plt.show()

c=df.select_dtypes(object)
#print(c)

#trasnform in numerical
encoder=LabelEncoder()
df['Number_Bikes']=encoder.fit_transform(df['Number_Bikes'])

c=df.dtypes
#print(c)

#groupings
x=df.groupby(['Season'])[['Number_Bikes']]
#print(x.mean())


#Aggregate
operations=['mean','sum','min','max']
a=df.groupby(['Year','Month'], as_index=False)[['Number_Bikes']].agg(operations)
print(a.reset_index())

df['Number_Bikes'].value_counts().sort_values(ascending=False).head(10)

sns.violinplot(x=df["Month"], y=df["Number_Bikes"], palette="Blues")
plt.show()



#when is the bike business doing the tbest  during the day. 

fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
df.groupby('Day_Time')['Item'].count().sort_values().plot(kind='bar')
plt.ylabel('Number_Bikes')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Business during the day')
plt.show()


sortbyday=df.groupby('Day_Time')['Item'].count().sort_values(ascending=False)

#business in the past months

df.groupby('Item')['Month'].count().plot(kind='bar')
plt.ylabel('Number_Bikess')
plt.title('Bikes number during the past months')
plt.show()

#extract month situation
Okt=df.loc[df['Month']=='Okt'].nunique()


#pivots. I should add the bike brand name so I can see which one is the pivot one
pivot1=df.pivot_table(index='Season',columns='Item', aggfunc={'Number_Bikes':'count'}).fillna(0)
pivot1['Max']=pivot1.idxmax(axis=1)
print(pivot1)

df.groupby('Item')['weekday'].count().plot(kind='bar')
plt.ylabel('Price')
plt.title('Bikes prices in the last days')


pivot2=df.pivot_table(index='Season',columns='Item', aggfunc={'Price':'count'}).fillna(0)
pivot2['Max']=pivot2.idxmax(axis=1)
print(pivot2)

pivotday=df.pivot_table(index='Day',columns='Item', aggfunc={'Price':'count'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)


#corr
plt.figure(figsize=(15,15))
sns.heatmap(df.corr(),annot=True,cmap='Blues_r',mask=np.triu(df.corr(),k=1))



#heatmap
plt.figure(figsize=(10,5))
sns.heatmap(df.corr(),cmap='Accent_r')



hour=df[['Hour','Item','Number_Bikes','Price',]].copy()
plt.figure(figsize=(10,5))
sns.heatmap(hour.corr(),cmap='binary_r')



df = px.data.tips()
fig = px.density_heatmap(hour, x="Item", y="Hour", nbinsx=20, nbinsy=20, color_continuous_scale="Blues",title='2d histograms')
#plotly.offline.plot(fig, filename='bike')

df = px.data.tips()
fig = px.density_heatmap(hour, x="Item", y="Price", nbinsx=20, nbinsy=20, color_continuous_scale="Blues_r",title='2d histograms')
#plotly.offline.plot(fig, filename='bike')

fig = px.density_heatmap(hour, x="Item", y="Number_Bikes", nbinsx=20, nbinsy=20, color_continuous_scale="Blues_r",title='2d histograms')
#plotly.offline.plot(fig, filename='bike')

fig = px.density_heatmap(hour, x="Hour", y="Number_Bikes", nbinsx=20, nbinsy=20, color_continuous_scale="Blues_r",title='2d histograms')
#plotly.offline.plot(fig, filename='bike')
























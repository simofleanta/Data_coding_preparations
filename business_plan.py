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

#
encoder=LabelEncoder()
df['Sales']=encoder.fit_transform(df['Sales'])

#

sns.violinplot(x=df["Item"], y=df["Sales"], palette="Blues")
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

df.groupby('Month')['Sales'].sum().plot(kind='bar')
plt.ylabel('Sales')
plt.title('Bikes sales in the last months')
plt.show()

df.groupby('Year')['Sales'].sum().plot(kind='bar')
plt.ylabel('Sales')
plt.title('2019-2020 comparison')
plt.show()

#pivotations

pivot2=df.pivot_table(index='Season',columns='Item', aggfunc={'Sales':'count'}).fillna(0)
pivot2['Max']=pivot2.idxmax(axis=1)
print(pivot2)

pivotday=df.pivot_table(index='Day',columns='Item', aggfunc={'Sales':'count'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

pivotday_m=df.pivot_table(index='Day',columns=['Year','Month','Item'], aggfunc={'Sales':'sum'}).fillna(0)
pivotday_m['Max']=pivotday_m.idxmax(axis=1)
print(pivotday_m)

pivotday_min=df.pivot_table(index='Month',columns=['Year','Item'], aggfunc={'Sales':'min'}).fillna(0)
pivotday_min['Min']=pivotday_min.idxmin(axis=1)
print(pivotday_min)

#2019 situ

y19=df[df.Year==2019]

df['Sales']=encoder.fit_transform(df['Sales'])
sns.violinplot(x=y19["Item"], y=y19["Sales"], palette="Blues")
plt.show()

df['Sales']=encoder.fit_transform(df['Sales'])
sns.violinplot(x=y19["Month"], y=y19["Sales"], palette="Blues")
plt.show()

#Bikes situ in 2020  

y=df[df.Year==2020]
pivotday_min_2020=y.pivot_table(index='Month',columns=['Year','Item'], aggfunc={'Sales':'min'}).fillna(0)
pivotday_min_2020['Min']=pivotday_min_2020.idxmin(axis=1)
print(pivotday_min_2020)

pivotday_max_2020=y.pivot_table(index='Month',columns=['Year','Month','Item'], aggfunc={'Sales':'max'}).fillna(0)
pivotday_max_2020['Max']=pivotday_max_2020.idxmax(axis=1)
print(pivotday_max_2020)

#pivot day2 
day2=y[y.Day==2]
pivotday2_2020=y.pivot_table(index='Item',columns=['Month','Item'], aggfunc={'Sales':'max'}).fillna(0)
pivotday2_2020['Max']=pivotday2_2020.idxmax(axis=1)
print(pivotday2_2020)


encoder=LabelEncoder()
df['Sales']=encoder.fit_transform(df['Sales'])
sns.violinplot(x=y["Item"], y=y["Sales"], palette="Blues")
plt.show()

df['Sales']=encoder.fit_transform(df['Sales'])
sns.violinplot(x=y["Month"], y=y["Sales"], palette="Blues")
plt.show()

#avg bikes 2020

bike_d=y.groupby(['Item'])['Sales'].mean()
days=pd.DataFrame(data=bike_d)
bike_Item=days.sort_values(by='Sales',ascending=False,axis=0)

fig = px.bar(bike_Item, x="Sales", y=bike_Item.index, color='Sales',color_continuous_scale='Blues',title="Average sales per month")
plotly.offline.plot(fig, filename='bike')


#corr
plt.figure(figsize=(15,15))
sns.heatmap(df.corr(),annot=True,cmap='Blues_r',mask=np.triu(df.corr(),k=1))
plt.show()










































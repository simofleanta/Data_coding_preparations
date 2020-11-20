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

# Numerical
encoder=LabelEncoder()
df['Sales']=encoder.fit_transform(df['Sales'])
df['Number_Bikes']=encoder.fit_transform(df['Number_Bikes'])
df['Item']=encoder.fit_transform(df['Item'])

c=df.select_dtypes(object)
#print(c)

c=df.dtypes
#print(c)

#groupings
x=df.groupby(['Season'])[['Number_Bikes']]
#print(x.mean())

#sort 
df['Number_Bikes'].value_counts().sort_values(ascending=False).head(10)

df.groupby('Month')['Sales'].sum().plot(kind='bar')
plt.ylabel('Sales')
plt.title('Bikes sales in the last months')
plt.show()

#compare 2019-2020
df.groupby('Year')['Sales'].sum().plot(kind='bar')
plt.ylabel('Sales')
plt.title('2019-2020 comparison')
plt.show()

fig1 = px.bar(df, x="Item", y=["Sales","Year"],barmode='group', color='Year',color_continuous_scale='Blues',title="comparing items in years 2020-2019")
plotly.offline.plot(fig1, filename='bike')

fig = px.bar(df, x="Item", y=["Sales","Year"],barmode='stack', color='Year',color_continuous_scale='Blues',title="Bike stacked per years")
plotly.offline.plot(fig, filename='bike')

#avg sales/mth

bike_d=df.groupby(['Month'])['Sales'].mean()
days=pd.DataFrame(data=bike_d)
bike_Month=days.sort_values(by='Sales',ascending=False,axis=0)
print(bike_Month)

fig = px.bar(bike_Month, x="Sales", y=bike_Month.index, color='Sales',color_continuous_scale='Blues',title="Average sales per month")
plotly.offline.plot(fig, filename='bike')

#avg sales/year

bike_d=df.groupby(['Year'])['Sales'].mean()
days=pd.DataFrame(data=bike_d)
bike_Year=days.sort_values(by='Sales',ascending=False,axis=0)

fig = px.bar(bike_Year, x="Sales", y=bike_Year.index, color='Sales',color_continuous_scale='Blues',title="Average sales per month")
plotly.offline.plot(fig, filename='bike')

#avg bikes 
bike_d=df.groupby(['Item'])['Sales'].mean()
days=pd.DataFrame(data=bike_d)
bike_Item=days.sort_values(by='Sales',ascending=False,axis=0)

fig = px.bar(bike_Item, x="Sales", y=bike_Item.index, color='Sales',color_continuous_scale='Blues',title="Average sales per month")
plotly.offline.plot(fig, filename='bike')
























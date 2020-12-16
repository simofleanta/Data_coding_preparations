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
print(c.columns)
df=DataFrame(c.head(500))
print(df.head(500))


#roi 
investment=40000 #received investment 
bike_costs=Item_cost_month=df['Item_cost_month']
loss=Loss_item=df['Loss_item']
net_profit=bike_costs*12-loss

#subset
df['roi']=net_profit/investment*100
print(df.tail(5))

#profitability 
df['Cost_to_produce']=2000*df.Number_Bikes
df['Profitability']=df.Cost_to_produce-df.Sales
df['Profitability_p']=df.Profitability/df.Number_Bikes
print(df.columns)
print(df.head(3))

reg=df

df = px.data.tips()
fig = px.scatter(reg, x="roi", y="Profitability", trendline="ols")
#plotly.offline.plot(fig, filename='r')

df = px.data.tips()
fig = px.scatter(reg, x="Cost_to_produce", y="Profitability",color_continuous_scale='Viridis',trendline="ols")
#plotly.offline.plot(fig, filename='r')

fig = px.scatter(reg, x="Profitability", y="Sales", color="weather_forecast", opacity=0.5,trendline="lowess")
#plotly.offline.plot(fig, filename='r')


#Treck profitability trend
Treck=reg[reg.Item=='Treck']
fig = px.scatter(Treck, x="Item_cost_month", y="Sales", color_continuous_scale="Item", opacity=0.5,trendline="lowess")
#plotly.offline.plot(fig, filename='r')


df = px.data.gapminder().query("year == 2020")
fig = px.scatter(reg, x="roi", y="Cost_to_produce", color="Item", trendline="lowess")
plotly.offline.plot(fig, filename='r')












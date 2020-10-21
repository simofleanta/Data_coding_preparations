import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
 
#open the file
bikes=pd.read_csv('bikes_h.csv')
print(bikes.columns)
df=DataFrame(bikes)

print(df.head(3))

#extract column
cnt=df['cnt']
print(cnt.head(3))

Registered=df['registered']
Weekday=df['weekday']
Season=df['season']
Hr=df['hr']
Mnth=df['mnth']
Windspeed=df['windspeed']
Yr=df['yr']
Cnt=df['cnt']

#The later it is the higher number of bikes are registered
#Summer has the most registered bikes 
#the same trend goes for count

fig = go.Figure(data=go.Heatmap(
                   z=Registered,
                   x=Hr,
                   y=Season,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Bikes per hour season',
    xaxis_nticks=40)


fig = go.Figure(data=go.Heatmap(
                   z=Cnt,
                   x=Hr,
                   y=Season,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Bikes per hour season',
    xaxis_nticks=40)

plotly.offline.plot(fig, filename='bike')

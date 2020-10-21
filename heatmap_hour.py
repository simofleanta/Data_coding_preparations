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
Workingday=df['workingday']

#The later it is the higher number of bikes are registered
#Summer has the most registered bikes 
#the same trend goes for count

fig = go.Figure(data=go.Heatmap(
                   z=Registered,
                   x=Hr,
                   y=Season,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Bikes registered per hour season',
    xaxis_nticks=40)

#bikes count with season
fig = go.Figure(data=go.Heatmap(
                   z=Cnt,
                   x=Hr,
                   y=Season,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Bikes count per hour season',
    xaxis_nticks=40)


#the upper trend is valid here too
#in all scenarios bike concentretion falls oh h 07:00-19:00(midd-day)
#concentration fades on days Thursday and Sunday
fig = go.Figure(data=go.Heatmap(
                   z=Cnt,
                   x=Hr,
                   y=Weekday,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Bikes count per hour weekday',
    xaxis_nticks=40)

#More bikes counted at h 17 on working days
#on non working day at 13 h 

fig = go.Figure(data=go.Heatmap(
                   z=Cnt,
                   x=Hr,
                   y=Workingday,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Bikes count per weeking day in certain hours',
    xaxis_nticks=40)



fig = go.Figure(data=go.Heatmap(
                   z=Cnt,
                   x=Workingday,
                   y=Workingday,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Bikes count per weeking day in certain hours',
    xaxis_nticks=40)

plotly.offline.plot(fig, filename='bike')


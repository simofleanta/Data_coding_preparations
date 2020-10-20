import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
biked=pd.read_csv('bike_sharing_daily.csv')
print(biked.columns)
df=DataFrame(biked)

print(df.head(3))

registered=df['registered']
weekday=df['weekday']
season=df['season']

#bikes per day season

fig = go.Figure(data=go.Heatmap(
                   z=registered,
                   x=weekday,
                   y=season,
                   colorscale='Viridis'))

fig.update_layout(
    title='Registered bikes per day',
    xaxis_nticks=36)


plotly.offline.plot(fig, filename='bike')


#on windy weather biker day

registered=df['registered']
weekday=df['weekday']
season=df['season']
windspeed=df['windspeed']
mnth=df['mnth']
cnt=df['cnt']

fig = go.Figure(data=go.Heatmap(
                   z=registered,
                   x=windspeed,
                   y=season,
                   colorscale='blues'))

fig.update_layout(
    title='Registered bikes per day',
    xaxis_nticks=36)


plotly.offline.plot(fig, filename='bike')


bike_d=df.groupby(['season'])['cnt'].mean()
days=pd.DataFrame(data=bike_d)
bike_season=days.sort_values(by='cnt',ascending=False,axis=0)
print(bike_season)
data=bike_season.index
h=bike_season.index


fig = go.Figure(data=go.Heatmap(
                   z=cnt,
                   x=season,
                   y=h,
                   colorscale='ice'))

fig.update_layout(
    title='Correlation on freedom dataset',
    xaxis_nticks=40)

plotly.offline.plot(fig, filename='bike')


#see if bike cnt is bigger when windspeed is big
#heatmap on windspeed cnt and season
bike=df[['season','mnth','windspeed','cnt']].copy()

seadon=bike['season']
mnth=bike['mnth']
windspeed=bike['windspeed']
cnt=bike['cnt']

fig = go.Figure(data=go.Heatmap(
                   z=windspeed,
                   x=mnth,
                   y=cnt,
                   colorscale='ice'))

fig.update_layout(
    title='Correlation on freedom dataset',
    xaxis_nticks=40)

plotly.offline.plot(fig, filename='bike')

fig = go.Figure(data=go.Heatmap(
                   z=windspeed,
                   x=season,
                   y=cnt,
                   colorscale='Blues'))

fig.update_layout(
    title='Correlation on freedom dataset',
    xaxis_nticks=40)

plotly.offline.plot(fig, filename='bike')





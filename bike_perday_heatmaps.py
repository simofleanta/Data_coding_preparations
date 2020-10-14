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

fig.show()

#on windy weather biker day

registered=df['registered']
weekday=df['weekday']
season=df['season']
windspeed=df['windspeed']
mnth=df['mnth']

fig = go.Figure(data=go.Heatmap(
                   z=registered,
                   x=windspeed,
                   y=season,
                   colorscale='blues'))

fig.update_layout(
    title='Registered bikes per day',
    xaxis_nticks=36)


plotly.offline.plot(fig, filename='bike')

fig.show()


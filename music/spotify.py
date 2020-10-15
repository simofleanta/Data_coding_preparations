import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
s=pd.read_csv('data_by_year.csv')
print(s.columns)
df=DataFrame(s)

print(df.head(3))

year=df['year']
popularity=df['popularity']
duration_ms=df['duration_ms']
acousticness=df['acousticness']
key=df['key']
energy=['energy']
instrumentalness=df['instrumentalness']
liveness=df['liveness']
loudness=df['loudness']
speechiness=df['speechiness']
valence=df['valence']
tempo=df['tempo']
danceability=df['danceability']


# in 2020 music with a shorter duration have a higher popularity

"""fig = px.scatter(df, x="year", y="popularity", color="popularity",
                 size='duration_ms', hover_data=['popularity'],
                 color_continuous_scale='RdBu')

plotly.offline.plot(fig, filename='m')"""

#the more we increase in years the less people liked liveness
"""fig = go.Figure(data=go.Heatmap(
                   x=year,
                   y=popularity,
                   z=liveness,
                   colorscale='Viridis'))

fig.update_layout(
    title='Music_year',
    xaxis_nticks=18)


plotly.offline.plot(fig, filename='m')"""

#why

"""fig = go.Figure(data=go.Heatmap(
                   x=year,
                   y=liveness,
                   z=duration_ms,
                   colorscale='Viridis'))

fig.update_layout(
    title='Music_year',
    xaxis_nticks=18)


plotly.offline.plot(fig, filename='m')"""

"""fig = px.sunburst(df, path=['year', 'popularity'], values='tempo',
                  color='liveness', hover_data=['liveness'],
                  color_continuous_scale='blues',
                  color_continuous_midpoint=np.average(df['liveness'], weights=df['liveness']))

plotly.offline.plot(fig, filename='m')"""

"""fig = go.Figure(data=go.Heatmap(
                   x=year,
                   y=acousticness,
                   z=instrumentalness,
                   colorscale='Magma'))

fig.update_layout(
    title='evolution of acoutic music',
    xaxis_nticks=18)

plotly.offline.plot(fig, filename='m')"""

fig = px.scatter(df, x="year", y="energy", color="speechiness",
                 size='popularity', hover_data=['popularity'],
                 color_continuous_scale='RdBu', title='We love energic music')

plotly.offline.plot(fig, filename='m')














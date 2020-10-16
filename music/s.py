import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly

#open the file
s=pd.read_csv('data_by_genres.csv')
print(s.columns)
df=DataFrame(s)

print(df.head(3))

genres=df['genres']
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


fig = px.scatter(df, x="genres", y="popularity", color="liveness",
                 size='duration_ms', hover_data=['popularity'],
                 color_continuous_scale='RdBu')

plotly.offline.plot(fig, filename='m')

#


fig = px.scatter(df, x="genres", y="liveness", color="popularity",
                 size='duration_ms', hover_data=['popularity'],
                 color_continuous_scale='Sunset')

plotly.offline.plot(fig, filename='m')

#

fig=px.treemap(df,
path=[genres],
values=liveness,
color=popularity,
color_continuous_scale='RdYlBu',
title='genres popularity',
hover_name=genres
  
)

fig.update_layout(
    title_font_size=42,
    title_font_family='Arial'
)

plotly.offline.plot(fig, filename='Music perception')









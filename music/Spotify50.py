import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
 
#open the file
s=pd.read_csv('Spotify50.csv')
print(s.columns)
df=DataFrame(s)
print(df.head(3))

print(df.groupby('Genre').size())
print(df.groupby('Artist_Name').size())



fig3 = px.bar(df, x="Popularity", y="Genre",barmode='stack', color='Popularity', color_continuous_scale='Blues', title="Spotify genres popularity")
#plotly.offline.plot(fig3, filename='bike')


#mean pop genres
spot=df.groupby(['Genre'])['Popularity'].mean()
s=pd.DataFrame(data=spot)
spotify_genres=s.sort_values(by='Popularity',ascending=False,axis=0)
#print(spotify_genres)

fig = px.bar(spotify_genres, x="Popularity", y=spotify_genres.index, color='Popularity',color_continuous_scale='Blues',title="Mean popularity on spotify genres")
#plotly.offline.plot(fig, filename='bike')


#mean pop Loudness
spot=df.groupby(['Genre'])['Loudness_DB'].mean()
s=pd.DataFrame(data=spot)
genres_lodness=s.sort_values(by='Loudness_DB',ascending=False,axis=0)

fig = px.bar(genres_lodness, x="Loudness_DB", y=genres_lodness.index, color='Loudness_DB',color_continuous_scale='Blues',title="Mean loudness on spotify genres")
#plotly.offline.plot(fig, filename='bike')

fig = px.bar(df, x="Artist_Name", y=["Beat_Per_Minute","Loudness_DB"],barmode='stack', color='Loudness_DB',color_continuous_scale='Blues',title="BPM and Lodness based on artists")
#plotly.offline.plot(fig, filename='hap')

fig = px.bar(df, x="Track_Name", y=["Beat_Per_Minute","Length","Acousticness"],barmode='stack', color='Popularity',color_continuous_scale='Blues',title="BPM and Acousticness based on artists")
#plotly.offline.plot(fig, filename='hap')


#----------------------------------------------------------------------------------------
Loudness_DB=df['Loudness_DB']
Energy=df['Energy']
Artist_Name=df['Artist_Name']
Genre=df['Genre']
Beat_Per_Minute=df['Beat_Per_Minute']
Popularity=df['Popularity']
Speechiness=df['Speechiness']
Track_Name=df['Track_Name']

fig0 = go.Figure(data=go.Heatmap(
                   z=Beat_Per_Minute,
                   x=Popularity,
                   y=Genre,
                   colorscale='Blues',
                   ))

fig.update_layout(
    
    title='spotify',
    xaxis_nticks=40)

#plotly.offline.plot(fig0, filename='bike')

fig0 = go.Figure(data=go.Heatmap(
                   z=Energy,
                   x=Popularity,
                   y=Artist_Name,
                   colorscale='Blues',
                   ))

fig.update_layout(
    
    title='spotify',
    xaxis_nticks=40)

#plotly.offline.plot(fig0, filename='bike')

fig0 = go.Figure(data=go.Heatmap(
                   z=Loudness_DB,
                   x=Popularity,
                   y=Artist_Name,
                   colorscale='Blues',
                   ))

fig.update_layout(
    
    title='spotify',
    xaxis_nticks=40)

#plotly.offline.plot(fig0, filename='bike')

fig0 = go.Figure(data=go.Heatmap(
                   z=Loudness_DB,
                   x=Beat_Per_Minute,
                   y=Track_Name,
                   colorscale='Blues',
                   ))

fig.update_layout(    
    title='Correlation between Loudness and BPM by track name',
    xaxis_nticks=40)

#plotly.offline.plot(fig0, filename='bike')





#treemaps

fig=px.treemap(df,
path=[Genre],
values=Beat_Per_Minute,
color=Popularity,
color_continuous_scale='Blues',
title='Popularity of Beats per minute based on genres ',
  
)

fig.update_layout(
    title_font_size=25,
    title_font_family='Arial'
)
#plotly.offline.plot(fig, filename='bike')

    
    




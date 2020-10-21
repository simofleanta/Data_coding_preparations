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
plotly.offline.plot(fig, filename='bike')
    
    




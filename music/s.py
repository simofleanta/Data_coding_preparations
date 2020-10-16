import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly

#open the file
s=pd.read_csv('data_by_artist.csv')
print(s.columns)
df=DataFrame(s)

print(df.head(3))

artists=df['artists']
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
count=df['count']


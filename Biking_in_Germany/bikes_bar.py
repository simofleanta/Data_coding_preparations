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

bike_d=df.groupby(['season'])['cnt'].mean()
days=pd.DataFrame(data=bike_d)
bike_season=days.sort_values(by='cnt',ascending=False,axis=0)
print(bike_season)

fig = px.bar(bike_season, x="cnt", y=bike_season.index, color='cnt',color_continuous_scale='Teal',title="Counting bikes_season")
plotly.offline.plot(fig, filename='bike')

fig = px.bar(df, x="season", y=["cnt","windspeed"],barmode='stack', color='windspeed',color_continuous_scale='Blues',title="bike")

plotly.offline.plot(fig, filename='hap')




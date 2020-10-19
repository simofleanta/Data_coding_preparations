import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
h=pd.read_csv('2015.csv')
print(h.columns)
df=DataFrame(h)

print(df.head(3))

#create a mini dataset from where to take desired columns to create corrs through heatmaps
generosity=df[['Generosity','Family','Happiness Rank']].copy()
freedom=df[['Freedom','Happiness Score','Generosity']].copy()

heat1=generosity.corr()
plt.figure(figsize=(10,6))
sns.heatmap(heat1,annot=True, cmap='winter_r')


heat2=generosity.corr()
plt.figure(figsize=(10,6))
sns.heatmap(heat1,annot=True, cmap='Blues')




freedom=df[['Region','Freedom','Happiness Score','Generosity']].copy()
data=freedom
Score=freedom['Happiness Score']
free=freedom['Freedom']
gen=freedom['Generosity']
Reg=freedom['Region']

fig = go.Figure(data=go.Heatmap(
                   z=Score,
                   x=Reg,
                   y=free,
                   colorscale='agsunset'))

fig.update_layout(
    title='Correlation on freedom dataset',
    xaxis_nticks=40)


plotly.offline.plot(fig, filename='te')








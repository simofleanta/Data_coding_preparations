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
freedom2=df[['Freedom','Trust (Government Corruption)','Economy (GDP per Capita)']].copy()

heat1=generosity.corr()
plt.figure(figsize=(10,6))
sns.heatmap(heat1,annot=True, cmap='winter_r')


heat2=generosity.corr()
plt.figure(figsize=(10,6))
sns.heatmap(heat1,annot=True, cmap='Blues')


#heatmap on freedom dataset but fromm WE region

WE=df[df.Region =='Western Europe']
freedom=WE
Score=freedom['Happiness Score']
free=freedom['Freedom']
gen=freedom['Generosity']
Reg=freedom['Region']
Country=freedom['Country']

fig = go.Figure(data=go.Heatmap(
                   z=Score,
                   x=Country,
                   y=free,
                   colorscale='ice'))

fig.update_layout(
    title='Correlation on freedom dataset',
    xaxis_nticks=40)


#Correlation oN GDP and Trust'

WE=df[df.Region =='Western Europe']
freedom2=WE
data=freedom2

Score=freedom2['Happiness Score']
free=freedom2['Freedom']
Reg=freedom2['Region']
Country=freedom2['Country']
gdp=freedom2['Economy (GDP per Capita)']
T=freedom2['Trust (Government Corruption)']

data1=freedom2

fig = go.Figure(data=go.Heatmap(
                   z=gdp,
                   x=Country,
                   y=T,
                   colorscale='ice'))

fig.update_layout(
    title='Correlation oN GDP and Trust',
    xaxis_nticks=40)


plotly.offline.plot(fig, filename='happy')








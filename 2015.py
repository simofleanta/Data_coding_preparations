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


#treemap on the lowest happiness rank per global region

rank=df['Happiness Rank']
Score=df['Happiness Score']
StandardErr=df['Standard Error']
Generosity=df['Generosity']
Region=df['Region']
Country=df['Country']
Scores=df['Happiness Score']


fig = px.scatter(df, x="Region", y="Happiness Rank", color="Happiness Score",
                 size='Family', hover_data=['Happiness Score'],
                 color_continuous_scale='RdBu')

plotly.offline.plot(fig, filename='Happyness Rank')

#bubblechart on scores and rank

WE=df[df.Region =='Western Europe']
data=WE
Country=WE['Country']

size = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,110,120,130]
fig = go.Figure(data=[go.Scatter(
    x=Country, y=rank,
    mode='markers',
    marker=dict(size=size,
    color=[110, 120, 130, 140, 150, 160,170, 180, 190, 200, 210, 220,230],
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        showscale=True)
    )
])

plotly.offline.plot(fig, filename='m')

#bubble chart on countries in CE Europe
CE=df[df.Region =='Central and Eastern Europe']
data=CE
Country=CE['Country']

size = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,110,120,130]
fig = go.Figure(data=[go.Scatter(
    x=Country, y=rank,
    mode='markers',
    marker=dict(size=size,
    color=[110, 120, 130, 140, 150, 160,170, 180, 190, 200, 210, 220,230],
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        showscale=True)
    )
])

plotly.offline.plot(fig, filename='m')

# sunchart East Asia

EA=df[df.Region =='Eastern Asia']
dfS=EA
Country=EA['Country']
Freedom=EA['Freedom']


fig = px.sunburst(dfS, path=['Region','Happiness Rank','Country'], values='Happiness Score',
                  color='Happiness Score', hover_data=['Happiness Score'],
                  color_continuous_scale='blues',
                  color_continuous_midpoint=np.average(df['Happiness Score'], weights=df['Happiness Score']))

plotly.offline.plot(fig, filename='hap')

#barchart on freedom per region

fig = px.bar(df, x="Region", y="Freedom", color="Freedom", title="Freedom")
plotly.offline.plot(fig, filename='hap')

#barchart on freedom WE #wide format

WE=df[df.Region =='Western Europe']
Country=WE['Country']
data=df

fig = px.bar(df, x="Region", y=["Freedom","Generosity"], color='Freedom',color_continuous_scale='Blues',barmode='group',title="Freedom")

plotly.offline.plot(fig, filename='hap')

#stack chart on freedom SE and generosity

fig = px.bar(WE, x="Country", y=["Freedom","Generosity","Standard Error"],barmode='stack', color='Standard Error',color_continuous_scale='Blues',title="Freedom")

plotly.offline.plot(fig, filename='hap')





















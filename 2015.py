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


"""fig = px.sunburst(df, path=['Region','Happiness Rank','Country'], values='Happiness Score',
                  color='Happiness Score', hover_data=['Happiness Score'],
                  color_continuous_scale='blues',
                  color_continuous_midpoint=np.average(df['Happiness Score'], weights=df['Happiness Score']))

plotly.offline.plot(fig, filename='hap')"""

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

plotly.offline.plot(fig, filename='m')

"""fig=px.treemap(df,
path=[Region],
values=rank,
color=rank,
color_continuous_scale='RdBu',
title='Happiness',
  
)

fig.update_layout(
    title_font_size=42,
    title_font_family='Arial'
)
plotly.offline.plot(fig, filename='Happyness Rank')"""

#heatmap on scores and rank
"""fig = go.Figure(data=go.Heatmap(
                   z=rank,
                   x=Region,
                   y=Score,
                   colorscale='agsunset'))

fig.update_layout(
    title='Score',
    xaxis_nticks=20)


plotly.offline.plot(fig, filename='Scor')"""



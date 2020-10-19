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

#bubblechart on scores and rank

WE=df[df.Region =='Western Europe']
data=WE
Country=WE['Country']

size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40]
fig = go.Figure(data=[go.Scatter(
    x=Country, y=rank,
    mode='markers',
    marker=dict(size=size,
    color=[120, 125, 130, 135, 140, 145],
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        showscale=True)
    )
])

plotly.offline.plot(fig, filename='m')



# Scatter on happiness scores and rank based on global region with bubbles size on family

"""fig = px.scatter(df, x="Region", y="Happiness Rank", color="Happiness Score",
                 size='Family', hover_data=['Happiness Score'],
                 color_continuous_scale='RdBu')

plotly.offline.plot(fig, filename='m')"""



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

#treemap happiness indicators per global region

rank=df['Happiness Rank']
Score=df['Happiness Score']
StandardErr=df['Standard Error']
Generosity=df['Generosity']
Region=df['Region']

fig=px.treemap(df,
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
plotly.offline.plot(fig, filename='Happyness Rank')




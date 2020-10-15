import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
px=pd.read_csv('heatmap_px.csv')
print(px.columns)
df=DataFrame(px)

print(df.head(3))

#heatmap
yr=df['yr']
company=df['company']
px=df['px']

"""fig = go.Figure(data=go.Heatmap(
                   z=px,
                   x=company,
                   y=yr,
                   colorscale='Blues'))

fig.update_layout(
    title='MSCI watchlist companies prices 2017-2019',
    xaxis_nticks=18)

plotly.offline.plot(fig, filename='px')

fig.show()"""

#sunburst

fig = px.sunburst(df, path=['yr'], values='px',
                  color='px', hover_data=['yr'],
                  color_continuous_scale='peach',
                  maxdepth=2,
                  color_continuous_midpoint=np.average(df['px'], weights=df['px']))

plotly.offline.plot(fig, filename='Company sunburst on years')

fig.show()






"""

fig = px.sunburst(df, path=['weekday','mnth','season'], values='cnt',
                  color='cnt', hover_data=['cnt'],
                  color_continuous_scale='peach',
                  maxdepth=2,
                  color_continuous_midpoint=np.average(df['cnt'], weights=df['cnt']))

plotly.offline.plot(fig, filename='bikes on a day')

fig.show()"""






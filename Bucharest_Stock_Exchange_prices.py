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


el=df[df.company=='EL']
print(el)


fig = go.Figure(data=go.Heatmap(
                   z=px,
                   x=company,
                   y=yr,
                   colorscale='Blues'))

fig.update_layout(
    title='MSCI watchlist companies prices 2017-2019',
    xaxis_nticks=18)

plotly.offline.plot(fig, filename='px')

fig.show()











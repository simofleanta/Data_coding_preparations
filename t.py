import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
t=pd.read_csv('TSLA.csv')
print(t.columns)
df=DataFrame(t)

print(df.head(3))

Date=df['Date']
Close=df['Close']
Open=df['Open']
Volume=df['Volume']



"""fig = go.Figure(data=go.Heatmap(
                   z=Open,
                   x=Close,
                   y=Date,
                   colorscale='Viridis'))

fig.update_layout(
    title='Tsls',
    xaxis_nticks=36)


plotly.offline.plot(fig, filename='te')"""



"""fig = px.sunburst(df, path=['Date','Volume'], values='Close',
                  color='Open', hover_data=['Close'],
                  color_continuous_scale='blues',
                  color_continuous_midpoint=np.average(df['Close'], weights=df['Close']))

plotly.offline.plot(fig, filename='ts')"""




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





#sunburst season and weekday
fig = px.sunburst(df, path=['weekday','mnth','season'], values='cnt',
                  color='cnt', hover_data=['cnt'],
                  color_continuous_scale='peach',
                  maxdepth=2,
                  color_continuous_midpoint=np.average(df['cnt'], weights=df['cnt']))

plotly.offline.plot(fig, filename='bikes on a day')

fig.show()


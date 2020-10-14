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
"""fig = px.sunburst(df, path=['County'], values='Voters',
                  color='Voters', hover_data=['Voters'],
                  color_continuous_scale='dense',
                  maxdepth=2,
                  color_continuous_midpoint=np.average(df['Voters'], weights=df['Voters']))

plotly.offline.plot(fig, filename='sun')

fig.show()"""
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


fig = px.sunburst(df, path=['Region','Happiness Rank','Country'], values='Happiness Score',
                  color='Happiness Score', hover_data=['Happiness Score'],
                  color_continuous_scale='blues',
                  color_continuous_midpoint=np.average(df['Happiness Score'], weights=df['Happiness Score']))

plotly.offline.plot(fig, filename='hap')


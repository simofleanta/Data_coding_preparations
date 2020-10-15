import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
c=pd.read_csv('covid_de.csv')
print(c.columns)
df=DataFrame(c)




state=df['state']
county=df['county']
age_g=df['age_group']
gender=df['gender']
cases=df['cases']
deaths=df['deaths']
recovered=df['recovered']


Thueringen=df[df.state=='Thueringen']
print(Thueringen)


fig = go.Figure(data=go.Heatmap(                   
                   x=state,
                   y=recovered,
                   z=deaths,
                   colorscale='Tealgrn'))

fig.update_layout(
    title='Recovered_Germany 2020',
    xaxis_nticks=18)


plotly.offline.plot(fig, filename='recovered')


fig=px.treemap(df,
path=[state],
values=recovered,
color=recovered,
color_continuous_scale='Blues',
title='Recovered in DE',
hover_name=recovered
  
)

fig.update_layout(
    title_font_size=42,
    title_font_family='Arial'
)

plotly.offline.plot(fig, filename='Recovered')

#Thueringen

sns.violinplot(x=df["age_group"], y=Thueringen["cases"], color='purple')
plt.show()

sns.violinplot(x=df["age_group"], y=Thueringen["recovered"], color='purple')
plt.show()

sns.violinplot(x=df["age_group"], y=Thueringen["deaths"], color='purple')
plt.show()






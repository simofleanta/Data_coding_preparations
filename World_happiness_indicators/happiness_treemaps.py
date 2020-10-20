import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly


#open the file
happy=pd.read_csv('2020.csv')
print(happy.columns)
df=DataFrame(happy)
print(df.head(3))


#--------------------------WestEu-----------------------#


#extract global region
WestEu=df[df.Regional_indicator=='Western_Europe']
print(WestEu)
#treemap

Country=WestEu['Country_name']
Health=WestEu['Healthy_life_expectancy']

fig=px.treemap(WestEu,
path=[Country],
values=Health,
color=Health,
color_continuous_scale='Teal',
title='Health_life_expectancy accross WEST EU Countries',
  
)

fig.update_layout(
    title_font_size=42,
    title_font_family='Arial'
)
plotly.offline.plot(fig, filename='Healthy_life_expectancy in West Eu')

#generosity

Country=WestEu['Country_name']
Generosity=WestEu['Generosity']

fig=px.treemap(WestEu,
path=[Country],
values=Generosity,
color=Generosity,
color_continuous_scale='Teal',
title='Perception_on_generosity',
hover_name=Generosity
  
)

fig.update_layout(
    title_font_size=42,
    title_font_family='Arial'
)

plotly.offline.plot(fig, filename='Generosity perception in Central Eu')







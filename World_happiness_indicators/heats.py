import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
happy=pd.read_csv('2020.csv')
print(happy.columns)
df=DataFrame(happy)
print(df.head(3))

WestEu=df[df.Regional_indicator=='Western_Europe']
#print(WestEu)
Central_and_Eastern_Europe=df[df.Regional_indicator=='Central_and_Eastern_Europe']


regions=WestEu[['Regional_indicator','Country_name','Generosity','Logged_GDP_perCapita','Freedom_to_make_life_choices']].copy()

Regions=regions['Regional_indicator']
Generosity=regions['Generosity']
Logged_GDP=regions['Logged_GDP_perCapita']
Freedom_to_make_life_choices=regions['Freedom_to_make_life_choices']
Country_name=regions['Country_name']


fig = go.Figure(data=go.Heatmap(
                   z=Generosity,
                   x=Country_name,
                   y=Logged_GDP,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Correlation on Generosity and logged gdp per countries in WE',
    xaxis_nticks=40)
plotly.offline.plot(fig, filename='bike')

#the higher the gdp the lower perception of generosity (higher y, lower z)

#CE
regions=Central_and_Eastern_Europe[['Regional_indicator','Country_name','Generosity','Logged_GDP_perCapita','Freedom_to_make_life_choices']].copy()

Regions=regions['Regional_indicator']
Generosity=regions['Generosity']
Logged_GDP=regions['Logged_GDP_perCapita']
Freedom_to_make_life_choices=regions['Freedom_to_make_life_choices']
Country_name=regions['Country_name']


fig = go.Figure(data=go.Heatmap(
                   z=Generosity,
                   x=Country_name,
                   y=Logged_GDP,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Correlation on Generosity and logged gdp per countries CE',
    xaxis_nticks=40)

plotly.offline.plot(fig, filename='bike')



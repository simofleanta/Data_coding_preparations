
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


#SUNBURST - Freedom_to_make_life_choices

fig = px.sunburst(df, path=['Regional_indicator','Country_name'], values='Freedom_to_make_life_choices',
                  color='Freedom_to_make_life_choices', hover_data=['Freedom_to_make_life_choices'],
                  color_continuous_scale='blues',
                  title='Freedom to make life choices in the world',
                  color_continuous_midpoint=np.average(df['Freedom_to_make_life_choices'], weights=df['Freedom_to_make_life_choices']))

plotly.offline.plot(fig, filename='sun')



#SUNBURST - Perceptions_of_corruption

fig = px.sunburst(df, path=['Regional_indicator','Country_name'], values='Perceptions_of_corruption',
                  color='Perceptions_of_corruption', hover_data=['Perceptions_of_corruption'],
                  color_continuous_scale='bluered',
                  title='Perception of corruption in the world',
                  color_continuous_midpoint=np.average(df['Perceptions_of_corruption'], weights=df['Perceptions_of_corruption']))

plotly.offline.plot(fig, filename='sun')



#SUNBURST - Logged_GDP_perCapita

fig = px.sunburst(df, path=['Regional_indicator','Country_name'], values='Logged_GDP_perCapita',
                  color='Logged_GDP_perCapita', hover_data=['Logged_GDP_perCapita'],
                  color_continuous_scale='portland',
                  title='GDP per Capita acorss regions and countries',
                  color_continuous_midpoint=np.average(df['Logged_GDP_perCapita'], weights=df['Logged_GDP_perCapita']))

plotly.offline.plot(fig, filename='sun')



#SUNBURST - Healthy_life_expectancy

fig = px.sunburst(df, path=['Regional_indicator','Country_name'], values='Healthy_life_expectancy',
                  color='Healthy_life_expectancy', hover_data=['Healthy_life_expectancy'],
                  color_continuous_scale='blues',
                  title='Healthy_life_expectancy',
                  color_continuous_midpoint=np.average(df['Healthy_life_expectancy'], weights=df['Healthy_life_expectancy']))

plotly.offline.plot(fig, filename='sun')

















































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

#Charts_for_all_df

#violinchart

sns.violinplot(x=df["Freedom_to_make_life_choices"], y=df["Regional_indicator"], color='purple')
plt.show()

sns.pairplot(df, vars=['Freedom_to_make_life_choices','Logged_GDP_perCapita'])
plt.show()

Scatter = sns.lmplot(data=df, x='Explained_by_Log_GDP_per_capita', y='Social_support',
                 fit_reg=False)
plt.show()

vis=sns.boxplot(data=df, x='Freedom_to_make_life_choices',y='Regional_indicator', palette='Reds')
plt.show()

#--------------------------WestEu-----------------------#


#extract global region
WestEu=df[df.Regional_indicator=='Western_Europe']
print(WestEu)

#chart it scatter
sns.pairplot(WestEu, vars=['Freedom_to_make_life_choices','Logged_GDP_perCapita'])
plt.show()



#---------------------------------------------------------
#perception on generosity treemap

Country=WestEu['Country_name']
Generosity=WestEu['Generosity']

fig=px.treemap(WestEu,
path=[Country],
values=Generosity,
color=Generosity,
color_continuous_scale='RdYlBu',
title='Perception_on_generosity',
hover_name=Generosity
  
)

fig.update_layout(
    title_font_size=42,
    title_font_family='Arial'
)

plotly.offline.plot(fig, filename='Generosity perception in Central Eu')
fig.show()

#--------------------------------------------------------------------------------------------
#SUNBURST - Freedom_to_make_life_choices

fig = px.sunburst(df, path=['Regional_indicator','Country_name'], values='Freedom_to_make_life_choices',
                  color='Freedom_to_make_life_choices', hover_data=['Freedom_to_make_life_choices'],
                  color_continuous_scale='blues',
                  color_continuous_midpoint=np.average(df['Freedom_to_make_life_choices'], weights=df['Freedom_to_make_life_choices']))

plotly.offline.plot(fig, filename='sun')

fig.show()

#SUNBURST - Perceptions_of_corruption

fig = px.sunburst(df, path=['Regional_indicator','Country_name'], values='Perceptions_of_corruption',
                  color='Perceptions_of_corruption', hover_data=['Perceptions_of_corruption'],
                  color_continuous_scale='bluered',
                  color_continuous_midpoint=np.average(df['Perceptions_of_corruption'], weights=df['Perceptions_of_corruption']))

plotly.offline.plot(fig, filename='sun')

fig.show()

#SUNBURST - Logged_GDP_perCapita

fig = px.sunburst(df, path=['Regional_indicator','Country_name'], values='Logged_GDP_perCapita',
                  color='Logged_GDP_perCapita', hover_data=['Logged_GDP_perCapita'],
                  color_continuous_scale='portland',
                  color_continuous_midpoint=np.average(df['Logged_GDP_perCapita'], weights=df['Logged_GDP_perCapita']))

plotly.offline.plot(fig, filename='sun')

fig.show()

#SUNBURST - Healthy_life_expectancy

fig = px.sunburst(df, path=['Regional_indicator','Country_name'], values='Healthy_life_expectancy',
                  color='Healthy_life_expectancy', hover_data=['Healthy_life_expectancy'],
                  color_continuous_scale='blues',
                  color_continuous_midpoint=np.average(df['Healthy_life_expectancy'], weights=df['Healthy_life_expectancy']))

plotly.offline.plot(fig, filename='sun')

fig.show()


#--------------------------------SouthEastAsia-----------------------------------------------


SouthEast_Asia=df[df.Regional_indicator=='Purples']
print(SouthEast_Asia)

plt.figure(figsize=(5,5))
sns.heatmap(SouthEast_Asia.corr())
plt.show()

sns.pairplot(SouthEast_Asia, vars=['Freedom_to_make_life_choices','Logged_GDP_perCapita'])
plt.show()

#--------------------------------CentralEast-----------------------------------------------

Central_and_Eastern_Europe=df[df.Regional_indicator=='Central_and_Eastern_Europe']
print(Central_and_Eastern_Europe)

plt.figure(figsize=(5,5))
sns.heatmap(Central_and_Eastern_Europe.corr(), cmap='YlOrBr')
plt.show()

sns.pairplot(Central_and_Eastern_Europe, vars=['Freedom_to_make_life_choices','Logged_GDP_perCapita'])
plt.show()

























































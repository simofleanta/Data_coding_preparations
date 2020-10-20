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


#extract global region
WestEu=df[df.Regional_indicator=='Western_Europe']
print(WestEu)
#treemap


#heatmap matplotlib

happy=WestEu[['Healthy_life_expectancy','Social_support','Perceptions_of_corruption','Country_name']].copy()
economy_generosity=WestEu[['Country_name','Generosity','Logged_GDP_perCapita','Healthy_life_expectancy']].copy()

#heat1
Health=happy['Healthy_life_expectancy']
Support=happy['Social_support']
Corruption=happy['Perceptions_of_corruption']
Country=happy['Country_name']

plt.figure(figsize=(5,5))
sns.heatmap(happy.corr(), cmap='Blues')
plt.show()

#heat2
Country=economy_generosity['Country_name']
Health=economy_generosity['Healthy_life_expectancy']
Generosity=economy_generosity['Generosity']
Economy=economy_generosity['Logged_GDP_perCapita']

plt.figure(figsize=(5,5))
sns.heatmap(economy_generosity.corr(), cmap='Purples_r')
plt.show()





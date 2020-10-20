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
Health=happy['Healthy_life_expectancy']
Support=happy['Social_support']
Corruption=happy['Perceptions_of_corruption']
Country=happy['Country_name']

plt.figure(figsize=(5,5))
sns.heatmap(happy.corr(), cmap='Blues')
plt.show()
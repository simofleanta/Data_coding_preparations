
import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
#open the file
happy=pd.read_csv('2020.csv')
print(happy.columns)
df=DataFrame(happy)

print(df.head(3))

#extract column
Health_expectancy=df['Healthy_life_expectancy']
print(Health_expectancy.head(3))

Country_name=df['Country_name']
print(Country_name.head(3))

Region=df['Regional_indicator']
print(Region.head(3))

#extract country
F=df[df.Country_name=='Finland']
print(F)


#pieChart
"""fig = px.pie(df, values='Social_support', names='Regional_indicator', title='Social Support regionWise',height=550)
fig.show()"""

Row_numbers, Column_numbers = df.shape
print("The number of countries in the dataset =",Row_numbers)
print("The number of parameters for happiness =",Column_numbers)

boxplot = sns.boxplot(data=df, x="Freedom_to_make_life_choices", y="Regional_indicator", palette='Blues')
plt.show()


vissual3 = sns.pairplot(df, vars=['Healthy_life_expectancy','Social_support'])
plt.show()

season = sns.lmplot(data=df, x='Explained_by_Log_GDP_per_capita', y='Healthy_life_expectancy',
                 fit_reg=False)
plt.show()

#--------------------------Log_GDP_per_capita  and Healthy_life_expectancy based on global region-----------------------#

"""West Europe"""
WestEu=df[df.Regional_indicator=='Western_Europe']
print(WestEu)

season = sns.lmplot(data=WestEu, x='Explained_by_Log_GDP_per_capita', y='Healthy_life_expectancy',
                 fit_reg=False)
plt.show()

"""North_America_and_ANZ"""

NorthAmerica=df[df.Regional_indicator=='North_America_and_ANZ']
print(NorthAmerica)

season = sns.lmplot(data=NorthAmerica, x='Explained_by_Log_GDP_per_capita', y='Healthy_life_expectancy',
                 fit_reg=False)
plt.show()

"""Central and East Eu"""

CentralEastEu=df[df.Regional_indicator=='Central_and_Eastern_Europe']
print(CentralEastEu)

CentralEastEu = sns.lmplot(data=CentralEastEu, x='Explained_by_Log_GDP_per_capita', y='Healthy_life_expectancy',
                 fit_reg=False)
plt.show()














































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

#extract country
F=df[df.Country_name=='Finland']
print(F)


#pieChart
fig = px.pie(df, values='Social_support', names='Regional_indicator', title='Social Support regionWise',height=550)
fig.show()

Row_numbers, Column_numbers = df.shape
print("The number of countries in the dataset =",Row_numbers)
print("The number of parameters for happiness =",Column_numbers)

boxplot = sns.boxplot(data=df, x="Freedom_to_make_life_choices", y="Regional_indicator", palette='Blues')
plt.show()


#check for null values#all is fine
print(df.isnull().sum())




































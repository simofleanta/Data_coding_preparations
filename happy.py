
import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import stats
 
#open the file
happy=pd.read_csv('2020.csv')
print(happy.columns)
df=DataFrame(happy)

print(df.head(3))

#extract country
F=df[df.Country_name=='Finland']
print(F)

#extract column
Health_expectancy=df['Healthy_life_expectancy']
print(Health_expectancy.head(3))

Country_name=df['Country_name']
print(Country_name.head(3))


"""Generosity=df['Explained_by_Generosity']
print(Generosity.head(3))"""
























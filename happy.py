
import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
 
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

Row_numbers, Column_numbers = df.shape
print("The number of countries in the dataset =",Row_numbers)
print("The number of parameters for happiness =",Column_numbers)



vissual2 = sns.lmplot(data=df, x='Regional_indicator', y='Freedom_to_make_life_choices',
                 fit_reg=False)

plt.show()

print(df.isnull().sum())


"""fig = px.bar(df, x='Regional_indicator', y='Freedom_to_make_life_choices',color='Freedom_to_make_life_choices',height=800)
fig.update_layout(title='Countries in descending order of Freedom_to_make_life_choices',titlefont_size=20)
fig.show()"""
































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

#rownumbers

Row_numbers, Column_numbers = df.shape
print("The number of countries in the dataset =",Row_numbers)
print("The number of parameters for happiness =",Column_numbers)

sns.violinplot(x=df["Social_support"], y=df["Country_name"], color='purple')
plt.show()




"""In order to obtain charts more global regions will be extracted"""
#--------------------------WestEu-----------------------#


#extract global region
WestEu=df[df.Regional_indicator=='Western_Europe']
print(WestEu)

#chart it scatter
Scatter = sns.lmplot(data=WestEu, x='Explained_by_Log_GDP_per_capita', y='Healthy_life_expectancy',
                 fit_reg=False)
plt.show()

#violinchart
sns.violinplot(x=WestEu["Social_support"], y=df["Country_name"], color='purple')
plt.show()

#heatmap
plt.figure(figsize=(5,5))
sns.heatmap(WestEu.corr(), cmap='Blues')
plt.show()

#pieChart
fig = px.pie(WestEu, values='Freedom_to_make_life_choices', names='Country_name', title='Region-wise economy',height=550)
fig.show()

#barchart
fig = px.bar(WestEu, x='Country_name', y='Freedom_to_make_life_choices',color='Freedom_to_make_life_choices',height=800)
fig.update_layout(title='Freedoom',titlefont_size=20)
fig.show()

#--------------------------------CentralEastEu---------------------------

CentralEastEu=df[df.Regional_indicator=='Central_and_Eastern_Europe']
print(CentralEastEu)

plt.figure(figsize=(5,5))
sns.heatmap(CentralEastEu.corr(), cmap='Blues')
plt.show()





















































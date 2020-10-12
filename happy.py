
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


sns.violinplot(x=df["Freedom_to_make_life_choices"], y=df["Regional_indicator"], color='purple')
plt.show()

sns.pairplot(df, vars=['Freedom_to_make_life_choices','Logged_GDP_perCapita'])
plt.show()

Scatter = sns.lmplot(data=df, x='Explained_by_Log_GDP_per_capita', y='Social_support',
                 fit_reg=False)

vis=sns.boxplot(data=df, x='Freedom_to_make_life_choices',y='Regional_indicator', palette='Reds')
plt.show()


#rownumbers

Row_numbers, Column_numbers = df.shape
print("The number of countries in the dataset =",Row_numbers)
print("The number of parameters for happiness =",Column_numbers)


"""In order to obtain charts more global regions will be extracted"""
#--------------------------WestEu-----------------------#


#extract global region
WestEu=df[df.Regional_indicator=='Western_Europe']
print(WestEu)

#chart it scatter
sns.pairplot(WestEu, vars=['Freedom_to_make_life_choices','Logged_GDP_perCapita'])
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























































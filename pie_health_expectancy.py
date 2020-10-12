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

WestEu=df[df.Regional_indicator=='Western_Europe']
print(WestEu)














"""

values=df['Healthy_life_expectancy']
names=df['Regional_indicator']

fig=px.pie(df,
values=values,
names=names,
title='Health_expectancy_regionwise')

fig.update_traces(

textposition='inside',
textinfo='percent + label'
)

fig.show()


import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import stats
 
#open the file
biked=pd.read_csv('bike_sharing_daily.csv')
print(biked.columns)
df=DataFrame(biked)

print(df.head(3))

#extract column
cnt=df['cnt']
print(cnt.head(3))


#heatmap
plt.figure(figsize=(10,5))
sns.heatmap(df.corr(),cmap='Blues')
plt.show()

#pairplot
vissual3 = sns.pairplot(df, vars=['registered','cnt'])
plt.show()

#violin
sns.violinplot(x=df["season"], y=df["cnt"], palette="Blues")
plt.show()

sns.violinplot(x=df["mnth"], y=df["casual"], palette="Blues")
plt.show()

#boxplots
vis4= sns.boxplot(data=df, x="season", y="registered", palette='Blues')
plt.show()

vis4= sns.boxplot(data=df, x="mnth", y="registered", palette='Blues')
plt.show()

vis4= sns.boxplot(data=df, x="mnth", y="casual", palette='Blues')
plt.show()

#distplot
vis1 = sns.distplot(df["cnt"])
plt.show()

#implot-scatterdot
vissual2 = sns.lmplot(data=df, x='mnth', y='casual',
                 fit_reg=False)
plt.show()

vissual2 = sns.lmplot(data=df, x='mnth', y='cnt',
                 fit_reg=False)
plt.show()

season = sns.lmplot(data=df, x='season', y='cnt',
                 fit_reg=False)
plt.show()"""















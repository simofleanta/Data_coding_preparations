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

h=WestEu.groupby(['Country_name'])['Perceptions_of_corruption'].mean()
hap=pd.DataFrame(data=h)
happy=hap.sort_values(by='Perceptions_of_corruption',ascending=False,axis=0)
print(happy)

fig = px.bar(happy, x="Perceptions_of_corruption", y=happy.index, color='Perceptions_of_corruption',color_continuous_scale='Teal',title="Perception of corruption in Western EU")
plotly.offline.plot(fig, filename='happy')

#------------------------------------Central and Eastern EU------------------------

Central_and_Eastern_Europe=df[df.Regional_indicator=='Central_and_Eastern_Europe']

h=Central_and_Eastern_Europe.groupby(['Country_name'])['Perceptions_of_corruption'].mean()
hap=pd.DataFrame(data=h)
happyCE=hap.sort_values(by='Perceptions_of_corruption',ascending=False,axis=0)
print(happyCE)

fig = px.bar(happyCE, x="Perceptions_of_corruption", y=happyCE.index, color='Perceptions_of_corruption',color_continuous_scale='Teal',title="Perception of corruption in Central and Eastern EU")
plotly.offline.plot(fig, filename='happy')



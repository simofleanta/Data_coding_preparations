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
#print(WestEu)

h=WestEu.groupby(['Country_name'])['Perceptions_of_corruption'].mean()
hap=pd.DataFrame(data=h)
happy_corr=hap.sort_values(by='Perceptions_of_corruption',ascending=False,axis=0)
#print(happy_corr)

fig = px.bar(happy_corr, x="Perceptions_of_corruption", y=happy_corr.index, color='Perceptions_of_corruption',color_continuous_scale='Teal',title="Perception of corruption in West EU")
"""plotly.offline.plot(fig, filename='happy')"""


h=WestEu.groupby(['Country_name'])['Generosity'].mean()
hap=pd.DataFrame(data=h)
happy=hap.sort_values(by='Generosity',ascending=False,axis=0)


fig = px.bar(happy, x="Generosity", y=happy.index, color='Generosity',color_continuous_scale='Teal',title="Generosity in Western EU")
"""plotly.offline.plot(fig, filename='happy')"""



#------------------------------------Central and Eastern EU------------------------

Central_and_Eastern_Europe=df[df.Regional_indicator=='Central_and_Eastern_Europe']

h=Central_and_Eastern_Europe.groupby(['Country_name'])['Perceptions_of_corruption'].mean()
hap=pd.DataFrame(data=h)
happyCE=hap.sort_values(by='Perceptions_of_corruption',ascending=False,axis=0)


fig = px.bar(happyCE, x="Perceptions_of_corruption", y=happyCE.index, color='Perceptions_of_corruption',color_continuous_scale='Teal',title="Perception of corruption in Central and Eastern EU")
"""plotly.offline.plot(fig, filename='happy')"""


h=Central_and_Eastern_Europe.groupby(['Country_name'])['Generosity'].mean()
hap=pd.DataFrame(data=h)
happy_gen=hap.sort_values(by='Generosity',ascending=False,axis=0)
#print(happy_gen)

fig = px.bar(happy_gen, x="Generosity", y=happy_gen.index, color='Generosity',color_continuous_scale='Teal',title="Perception of generosity in Central and Eastern EU")
"""plotly.offline.plot(fig, filename='happy')"""


# regions

fig = px.bar(df, x="Regional_indicator", y=["Generosity","Logged_GDP_perCapita"],barmode='stack', color='Logged_GDP_perCapita',color_continuous_scale='Blues',
title="Perception of generosity based on logged GDP per Capita")
plotly.offline.plot(fig, filename='hap')


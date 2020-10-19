import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
h=pd.read_csv('2015.csv')
print(h.columns)
df=DataFrame(h)

print(df.head(3))

#happiness Score per regions

"""df_scores=df.groupby(['Region'])['Happiness Score'].mean()
df_scores=pd.DataFrame(data=df_scores)
df_h_scores=df_scores.sort_values(by='Happiness Score',ascending=False,axis=0)
print(df_h_scores)

fig = px.bar(df_h_scores, x="Happiness Score", y=df_h_scores.index, color='Happiness Score',color_continuous_scale='Sunset',title="Happiness in different regions")
plotly.offline.plot(fig, filename='hap')"""

#happiness rank per regions

"""df_scores=df.groupby(['Region'])['Happiness Rank'].mean()
df_scores=pd.DataFrame(data=df_scores)
df_h_rank=df_scores.sort_values(by='Happiness Rank',ascending=False,axis=0)
print(df_h_rank)

fig = px.bar(df_h_rank, x="Happiness Rank", y=df_h_rank.index, color='Happiness Rank',color_continuous_scale='Sunset',title="Happiness rank in different regions")
plotly.offline.plot(fig, filename='hap')"""

#happiness/rank WE

WE=df[df.Region =='Western Europe']
Country=WE['Country']
print(WE)

WE_happiness=WE.groupby(['Country'])['Happiness Rank'].mean()
WE_happiness=pd.DataFrame(data=WE_happiness)
Happiness_rank=WE_happiness.sort_values(by='Happiness Rank',ascending=False,axis=0)
print(Happiness_rank)

fig = px.bar(Happiness_rank, x="Happiness Rank", y=Happiness_rank.index, color='Happiness Rank',color_continuous_scale='Sunset',title="Happiness rank in different regions")
plotly.offline.plot(fig, filename='hap')
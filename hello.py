import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
g=pd.read_csv('2017_german_election_party.csv')
#print(g.columns)
df=DataFrame(g)

#check dtypes
types=df.dtypes
#print(types)
#no missing_v
missing_v=df.isnull().sum()
#print(missing_v)
vc=df['party'].value_counts()
#print(vc)

#rename columns model
#de=df.rename(columns={'x.Name':'y_Name'},inplace=True)
#df.head()


#grouping stuff

#grouping by stuff

e=df.groupby('party')['votes_second_vote'].mean()
print(e)

d=df.groupby(['party'])['votes_first_vote'].sum().sort_values(ascending =False)[:5]

#reference columns for treemaps
area_id=df['area_id']
area_name=df['area_name']
votes_first_vote=df['votes_first_vote']
state=df['state']
party=df['party']
votes_second_vote=df['votes_second_vote']

#barcharts

fig = go.Figure(data=go.Heatmap(
                   z=votes_second_vote,
                   x=state,
                   y=party,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Votes in German elections 2017 heatmap',
    xaxis_nticks=40)

#plotly.offline.plot(fig, filename='votes')



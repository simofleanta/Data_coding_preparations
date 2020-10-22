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


#extract party


CDU=df[df.party=='Christlich.Demokratische.Union.Deutschlands']
print(CDU)

area_id=CDU['area_id']
area_name=CDU['area_name']
votes_first_vote=CDU['votes_first_vote']
State=CDU['state']
Party=CDU['party']
voteSecondVote=CDU['votes_second_vote']

v=CDU.groupby(['state'])['votes_second_vote'].mean()
el=pd.DataFrame(data=v)
Votes=el.sort_values(by='votes_second_vote',ascending=False,axis=0)
print(Votes)

fig = px.bar(Votes, x="votes_second_vote", y=Votes.index, color='votes_second_vote',color_continuous_scale='Blues',title="CDU 2nd votes")
#plotly.offline.plot(fig, filename='bike')


v=CDU.groupby(['state'])['votes_first_vote'].mean()
el=pd.DataFrame(data=v)
cduVotes=el.sort_values(by='votes_first_vote',ascending=False,axis=0)
print(cduVotes)

ig = px.bar(cduVotes, x="votes_first_vote", y=cduVotes.index, color='votes_first_vote',color_continuous_scale='Blues',title="CDU 1st votes")
#plotly.offline.plot(fig, filename='bike')


fig = px.bar(CDU, x="state", y=["votes_second_vote","votes_first_vote"],barmode='stack', color='votes_first_vote',color_continuous_scale='Blues',
title="CDU 1st and 2nd votes performance across states in Germany")
#plotly.offline.plot(fig, filename='hap')



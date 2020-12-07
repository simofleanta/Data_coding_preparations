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
h=pd.read_csv('2017_german_election_overall.csv')
#print(g.columns)
df=DataFrame(g)
valid=DataFrame(h)

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


#Groupings 
mean_party=df.groupby('party')['votes_second_vote'].mean()
print(mean_party)

first_vote_sort=df.groupby(['party'])['votes_first_vote'].sum().sort_values(ascending =False)[:5]

#reference columns for heatmaps
area_id=df['area_id']
area_name=df['area_name']
votes_first_vote=df['votes_first_vote']
state=df['state']
party=df['party']
votes_second_vote=df['votes_second_vote']


fig = go.Figure(data=go.Heatmap(
                   z=votes_second_vote,
                   x=state,
                   y=party,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Votes in German elections 2017 heatmap',
    xaxis_nticks=40)

#plotly.offline.plot(fig, filename='votes')

fig = go.Figure(data=go.Heatmap(
                   z=votes_first_vote,
                   x=state,
                   y=party,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Votes in German 1st votes 2017 heatmap',
    xaxis_nticks=40)

#plotly.offline.plot(fig, filename='votes')


fig = go.Figure(data=go.Heatmap(
                   z=votes_first_vote,
                   x=area_name,
                   y=party,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Votes in German 1st votes 2017 heatmap',
    xaxis_nticks=35,
    yaxis_nticks=30)

#plotly.offline.plot(fig, filename='votes')



#extract party and chart

CDU=df[df.party=='Christlich.Demokratische.Union.Deutschlands']
print(CDU)

area_id=CDU['area_id']
Area_name=CDU['area_name']
votes_first_vote=CDU['votes_first_vote']
State=CDU['state']
Party=CDU['party']
voteSecondVote=CDU['votes_second_vote']

fig = px.scatter(CDU, x="state", y="votes_second_vote", color="votes_second_vote",
                 size='votes_second_vote', hover_data=['votes_second_vote'],
                 color_continuous_scale='Blues',
                 title='CDU accross DE')

#plotly.offline.plot(fig, filename='votes')


#bar charts
v=CDU.groupby(['state'])['votes_second_vote'].mean()
el=pd.DataFrame(data=v)
Votes=el.sort_values(by='votes_second_vote',ascending=False,axis=0)
#print(Votes)

fig = px.bar(Votes, x="votes_second_vote", y=Votes.index, color='votes_second_vote',color_continuous_scale='Blues',title="CDU 2nd votes")
#plotly.offline.plot(fig, filename='bike')

v=CDU.groupby(['state'])['votes_first_vote'].mean()
el=pd.DataFrame(data=v)
cduVotes=el.sort_values(by='votes_first_vote',ascending=False,axis=0)
#print(cduVotes)

fig = px.bar(cduVotes, x="votes_first_vote", y=cduVotes.index, color='votes_first_vote',color_continuous_scale='Blues',title="CDU 1st votes")
#plotly.offline.plot(fig, filename='bike')

fig = px.bar(CDU, x="state", y=["votes_second_vote","votes_first_vote"],barmode='stack', color='votes_first_vote',color_continuous_scale='Blues',
title="CDU 1st and 2nd votes performance across states in Germany")
#plotly.offline.plot(fig, filename='hap')

# extract party and scatter 

AFD=df[df.party=='Alternative.für.Deutschland']

fig = px.scatter(AFD, x="state", y="votes_second_vote", color="votes_second_vote",
                 size='votes_second_vote', hover_data=['votes_second_vote'],
                 color_continuous_scale='Blues',
                 title='AFD across states')

#plotly.offline.plot(fig, filename='votes')


fig3 = px.bar(AFD, x="state", y=["state","votes_second_vote"],barmode='group', color='state',title="AFD grouped")
#plotly.offline.plot(fig3, filename='bike')


fig4 = px.bar(CDU, x="state", y=["state","votes_second_vote"],barmode='group', color='state',title="CDU grouped")
#plotly.offline.plot(fig4, filename='bike')



valid_first_votes=valid['valid_first_votes']
valid_second_votes=valid['valid_second_votes']
Area_name=valid['area_names']
invalid_first_votes=valid['invalid_first_votes']
State=valid['state']
registered=valid['registered.voters']
invalid_second_votes=valid['invalid_second_votes']
total_votes=valid['total_votes']

fig = go.Figure(data=go.Heatmap(
                   z=total_votes,
                   x=Area_name,
                   y=State,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Votes in German 1st votes 2017 heatmap',
    xaxis_nticks=35,
    yaxis_nticks=30)

#plotly.offline.plot(fig, filename='votes')

fig = px.scatter(valid, x="state", y="total_votes", color="total_votes",
                 size='valid_second_votes', hover_data=['valid_second_votes'],
                 color_continuous_scale='Blues',
                 title='Votes across states')

#plotly.offline.plot(fig, filename='votes')

fig = px.scatter(valid, x="state", y="total_votes", color="total_votes",
                 size='invalid_second_votes', hover_data=['invalid_second_votes'],
                 color_continuous_scale='Blues',
                 title='Invalid Votes across states')

#plotly.offline.plot(fig, filename='votes')

sns.violinplot(x=valid["state"], y=valid["total_votes"], palette="Blues")
plt.show()

#2d histogram
df = px.data.tips()
fig = px.density_heatmap(valid, x="state", y="total_votes", nbinsx=20, nbinsy=20, color_continuous_scale="YlOrRd",title='2d histograms on total votes in diff states')
#plotly.offline.plot(fig, filename='bikes on a day')








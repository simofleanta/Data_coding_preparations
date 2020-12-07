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
print(g.columns)
df=DataFrame(g)

print(df.head(3))

area=df['area_name']
state=df['state']
party=df['party']
votes1=df['votes_first_vote']
votes2=df['votes_second_vote']
area_id=['area_id']

fig = go.Figure(data=go.Heatmap(
                   z=votes2,
                   x=state,
                   y=party,
                   colorscale='Viridis'))

fig.update_layout(
    title='Votes in Germany 2017',
    xaxis_nticks=18)


plotly.offline.plot(fig, filename='votes_g')

fig.show()

#scatter

cdu=df[df.party=='Christlich.Demokratische.Union.Deutschlands']
afd=df[df.party=='Alternative.fÃ¼r.Deutschland']
B=df[df.state=='Berlin']

fig = px.scatter(cdu, x="state", y="votes_second_vote", color="votes_second_vote",
                 size='votes_second_vote', hover_data=['votes_second_vote'],
                 color_continuous_scale='Teal')

plotly.offline.plot(fig, filename='votes_S')


fig = px.scatter(B, x="party", y="votes_second_vote", color="votes_second_vote",
                 size='votes_first_vote', hover_data=['votes_first_vote'],
                 color_continuous_scale='Tealgrn')

plotly.offline.plot(fig, filename='votes_S')


fig = px.scatter(df, x="party", y="votes_second_vote", color="votes_second_vote",
                 size='votes_second_vote', hover_data=['votes_second_vote'])

plotly.offline.plot(fig, filename='votes_S')

#elections overall g

de=pd.read_csv('2017_german_election_overall.csv')
print(de.columns)
df=DataFrame(de)

print(df.head(3))
print(df.columns)

#Heatmaps

area=df['area_names']
state=df['state']
registered_voters=df['registered.voters']
valid_votes1=df['valid_first_votes']
invalid_second_votes=df['invalid_second_votes']
invalid_first_votes=df['invalid_first_votes']
valid_votes2=df['valid_second_votes']
total_votes=df['total_votes']

fig = go.Figure(data=go.Heatmap(                   
                   x=state,
                   y=valid_votes2,
                   z=registered_voters,
                   colorscale='RdBu'))

fig.update_layout(
    title='Presence of Votes in Germany 2017',
    xaxis_nticks=18)


plotly.offline.plot(fig, filename='votes_overall')

#invalid second
fig = go.Figure(data=go.Heatmap(                   
                   x=state,
                   y=invalid_second_votes,
                   z=registered_voters,
                   colorscale='Teal'))

fig.update_layout(
    title='Invalid second Votes in Germany 2017',
    xaxis_nticks=18)


plotly.offline.plot(fig, filename='votes_overall')

#invalid first

fig = go.Figure(data=go.Heatmap(                   
                   x=state,
                   y=invalid_first_votes,
                   z=registered_voters,
                   colorscale='Tealgrn'))

fig.update_layout(
    title='Invalid first Votes in Germany 2017',
    xaxis_nticks=18)


plotly.offline.plot(fig, filename='votes_overall')


fig = go.Figure(data=go.Scatter(
    x=party,
    y=['votes_second_vote'],
    mode='markers',
    marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3,4,5,6])
))
plotly.offline.plot(fig, filename='votes_overall')


















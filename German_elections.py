import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
"""g=pd.read_csv('2017_german_election_party.csv')
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

fig.show()"""

#elections overall g

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


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

freedom2=df[['Freedom','Region','Trust (Government Corruption)','Economy (GDP per Capita)','Happiness Rank']].copy()
print(freedom2)

region_gdp=df.groupby(['Region'])['Economy (GDP per Capita)'].mean()
gdp_r=pd.DataFrame(data=region_gdp)
gdp_region=gdp_r.sort_values(by='Economy (GDP per Capita)',ascending=False,axis=0)
print(gdp_region)

fig = px.bar(gdp_region, x="Economy (GDP per Capita)", y=gdp_region.index, color='Economy (GDP per Capita)',color_continuous_scale='Sunset',title="Happiness rank in different regions")
plotly.offline.plot(fig, filename='hap')


freedom=df['Freedom']
gdps=df['Economy (GDP per Capita)']
trust=df['Trust (Government Corruption)']
rank=df['Happiness Rank']
Regions=df['Region']
h=gdp_region.index
data=df


size = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,110,120,130]
fig = go.Figure(data=[go.Scatter(
    x=Regions, y=gdp_region.index,
    mode='markers',
    marker=dict(size=size,
    color=[110, 120, 130, 140, 150, 160,170, 180, 190, 200, 210, 220,230],
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        showscale=True)
    )
])

plotly.offline.plot(fig, filename='m')

CE=df[df.Region =='Central and Eastern Europe']
Country=CE['Country']
print(CE)

region_free=CE.groupby(['Region'])['Freedom'].mean()
free_r=pd.DataFrame(data=region_free)
free_region=free_r.sort_values(by='Freedom',ascending=False,axis=0)
print(free_region)

Countrys=CE['Country']
data=CE
j=free_region.index
size = [10, 20, 30, 40, 50, 100,110,120,130]
fig = go.Figure(data=[go.Scatter(
    x=Countrys, y=j,
    mode='markers',
    marker=dict(size=size,
    color=[110, 120, 130, 140, 150, 160,170, 18, 220,230],
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        showscale=True)
    )
])

plotly.offline.plot(fig, filename='m')













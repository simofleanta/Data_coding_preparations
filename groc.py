import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import sklearn.preprocessing
from sklearn.metrics import r2_score
import plotly.io as pio
import datetime
import plotly

df=pd.read_csv('Groceries_dataset.csv', parse_dates=['Date'])
print(df.head(3))

missing_v=df.isnull().any()
print(missing_v)
vc=df['Member_number'].value_counts()
#total prod
all = df['itemDescription'].unique()
print("Total:{}".format(len(all)))

#top5

def product_distribution(x,y,name=None,xaxis=None,yaxis=None):
    fig = go.Figure([
        go.Bar(x=x, y=y)
    ])

    fig.update_layout(
        title_text=name,
        xaxis_title=xaxis,
        yaxis_title=yaxis
    )
    
    plotly.offline.plot(fig, filename='bike')

x = df['itemDescription'].value_counts()
x = x.sort_values(ascending = False) 
x = x[:15]

product_distribution(x=x.index, y=x.values, yaxis="Count", xaxis="Products")









"""
m=df_g['Member_number']
d=df_g['Date']
item=df_g['itemDescription']


fig0 = go.Figure(data=go.Heatmap(
                   z=m,
                   x=d,
                   y=item,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Bikes registered per hour season',
    xaxis_nticks=40)

#plotly.offline.plot(fig0, filename='bike')

foods=df.groupby(['itemDescription'])['Member_number'].mean()
f=pd.DataFrame(data=foods)
groceries=f.sort_values(by='Member_number',ascending=False,axis=0)
print(groceries)

fig = px.bar(groceries, x="Member_number", y=groceries.index, color='Member_number',color_continuous_scale='Teal',title="Counting bikes_season")
plotly.offline.plot(fig, filename='bike') """






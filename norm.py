import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
 
#open the file
bikes=pd.read_csv('bikes_h.csv')
print(bikes.columns)
df=DataFrame(bikes)

#extract column
cnt=df['cnt']

#no missing_v
missing_v=df.isnull().sum()
vc=df['hr'].value_counts()
#check dtypes
types=df.dtypes

#function to fix dtatypes

def fixing_datatypes(df):
    """Fixing the datatypes""" 
    df['dteday'] = df['dteday'].astype('datetime64')
    df.loc[:,'season':'mnth'] = df.loc[:,'season':'mnth'].astype('category')
    df[['holiday','workingday']] = df[['holiday','workingday']].astype('bool')
    df[['weekday','weathersit']] = df[['weekday','weathersit']].astype('category')

   
    mapping_season = {1:"1_Winter", 2:"2_Spring", 3:"3_Summer", 4:"4_Fall" }
    mapping_weekdays = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 
                        4:"Thursday", 5:"Friday", 6:"Saturday"}
    mapping_weather = {1:"good", 2:"medium", 3:"poor", 4:"very_poor" }
    
    df["season"] = df.season.map(mapping_season)
    df["weekday"] = df.weekday.map(mapping_weekdays)
    df["weathersit"] = df.weathersit.map(mapping_weather)

    return df
    #call function
    df_hourly = fixing_datatypes(df_hourly)
#assigining function to df whith which will be going through analysis 
df=fixing_datatypes(df)
print(df.head(2))
#------------------------------------------------------------------------------------

#grouping by stuff

e=df.groupby('weekday')['cnt'].mean()
print(e)
ef=df.groupby('workingday')['cnt'].mean()
print(ef)
efg=df.groupby('weathersit')['cnt'].mean()
print(efg)
efgh=df.groupby('dteday')['cnt'].mean()
print(efgh)

#performing bar charts 

fig = px.bar(df, x="hr", y=["cnt","workingday"],barmode='group', color='workingday',title="bikes count per hour grouped on working day")
#plotly.offline.plot(fig, filename='bike')
fig1 = px.bar(df, x="hr", y=["cnt","weekday"],barmode='group', color='weekday',title="bike per hour grouped on weekdays")
#plotly.offline.plot(fig1, filename='bike')
fig2 = px.bar(df, x="hr", y=["cnt","weathersit"],barmode='group', color='weathersit',title="bike per hour grouped on weekdays")
#plotly.offline.plot(fig2, filename='bike')
fig3 = px.bar(df, x="hr", y=["cnt","mnth"],barmode='group', color='mnth',title="bike per hour grouped on weekdays")
#plotly.offline.plot(fig3, filename='bike')

#performing heat charts 

Registered=df['registered']
Weekday=df['weekday']
Season=df['season']
Hr=df['hr']
Mnth=df['mnth']
Windspeed=df['windspeed']
Yr=df['yr']
Cnt=df['cnt']
Workingday=df['workingday']
weathersit=df['weathersit']


fig0 = go.Figure(data=go.Heatmap(
                   z=Cnt,
                   x=Hr,
                   y=weathersit,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Bikes registered per hour season',
    xaxis_nticks=40)

#plotly.offline.plot(fig0, filename='bike')

fig = go.Figure(data=go.Heatmap(
                   z=Cnt,
                   x=Hr,
                   y=Weekday,
                   colorscale='Blues'))

fig.update_layout(
    
    title='Bikes count per weekday',
    xaxis_nticks=40)

plotly.offline.plot(fig, filename='bike')






   

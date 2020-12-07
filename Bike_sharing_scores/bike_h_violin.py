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

print(df.head(3))

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


#violin
sns.violinplot(x=df["workingday"], y=df["cnt"], palette="Blues")
plt.show()

sns.violinplot(x=df["weekday"], y=df["cnt"], palette="Blues")
plt.show()



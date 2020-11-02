
import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
import statistics
import stats

#open file
c=pd.read_csv('day.csv')
#print(c.columns)
df=DataFrame(c.head(3))
#print(df.head(10))

#check missing_v
missing_v=df.isnull().sum()
vc=df['cnt'].value_counts()
#print(vc)

#check dtypes before change
types=df.dtypes
#print(types)

#change area in cat
mnth_cat=df.mnth=pd.Categorical(df['mnth'], ordered=True)
weekday_cat=df.weekday=pd.Categorical(df['weekday'], ordered=True)
workingday_cat=df.workingday=pd.Categorical(df['workingday'], ordered=True)
season_cat=df.season=pd.Categorical(df['season'], ordered=True)
#check dtypes after change
types=df.dtypes


#groupings by
n=df.groupby('weekday',).cnt.mean()
P=df.groupby('mnth').cnt.mean()
P=df.groupby('season').cnt.mean()

#mean on a certain category
q=df[df.workingday==1].cnt.mean()
print(q)
s=df[df.season==1].cnt.mean()
print(s)

#mean
g=df.groupby('weekday')
print(g)

for weekday, weekday_df in g:
    print(weekday)
    print(weekday_df)

#open file
c=pd.read_csv('day.csv')
#print(c.columns)
df=DataFrame(c.head(3))
print(df.head(10))



f=['mean','max','min','count', 'std','var']
x=df.groupby(['weekday'], as_index=False)[['cnt']].agg(f)
print(x.reset_index())


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

#NORMALIZE DATA BEFORE ANALYSIS  using numpy :D
#print(en)
#normalizing data using lamda
#en=en.apply(lambda x: (x - x.min(axis=0))/(x.max(axis=0) - x.min(axis=0)))
#en=df['AEP_MW']
#date=df['Datetime']
#NORMALIZE DATA BEFORE ANALYSIS  using sklearn :D

#open the file
g=pd.read_csv('AEP_hourly.csv')
#print(g.columns)
df=DataFrame(g)
#print(df.columns)
#print(df.head(10))


#no missing_v
missing_v=df.isnull().sum()
#print(missing_v)
vc=df['Datetime'].value_counts()

#datetime
#df = pd.read_csv(df, index_col='Datetime', parse_dates=['Datetime'])
#df.head()



#group AEP_MW by datetime :)
e=df.groupby('Datetime')['AEP_MW'].mean()
#print(e.head(5))

df.plot(figsize=(16,4),legend=True)

plt.title('AEP hourly power consumption data - BEFORE NORMALIZATION')
#plt.show()



def normalize_data(df):
    scaler = sklearn.preprocessing.MinMaxScaler()
    df['AEP_MW']=scaler.fit_transform(df['AEP_MW'].values.reshape(-1,1))
    return df

df_norm = normalize_data(df)

shape=df_norm.shape
print(shape)
print(df_norm.head(3))


df.plot(figsize=(16,4),legend=True)

plt.title('AEP hourly power consumption data - AFTER NORMALIZATION:)')
#plt.show()

#chart 2d histograms on hourly energy consumption 2004-2018 :)

import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df_norm, x="Datetime", y="AEP_MW", nbinsx=20, nbinsy=20, color_continuous_scale="YlOrRd",title='2d histograms on hourly energy consumption 2004-2018 :)')
#plotly.offline.plot(fig, filename='bikes on a day')



######scatter groupby 



subject=df_norm['Datetime']
score =df_norm['AEP_MW']

data = [dict(
  type = 'scatter',
  x = subject,
  y = score,
  mode = 'markers',
  transforms = [dict(
    type = 'groupby',
    groups = subject,
    styles = [
        dict(target = 'Moe', value = dict(marker = dict(color = 'blue'))),
        dict(target = 'Larry', value = dict(marker = dict(color = 'red'))),
        dict(target = 'Curly', value = dict(marker = dict(color = 'black')))
    ]
  )]
)]

fig_dict = dict(data=data)
#pio.show(fig_dict, validate=False)
plotly.offline.plot(fig_dict, validate=False)
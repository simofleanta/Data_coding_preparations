import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import numpy as np
import plotly
import statistics
import plotly.express as px
import stats
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import plotly.express as px
from datetime import datetime



active=pd.read_csv('active_users.csv')
print(active.columns)
df=DataFrame(active)
print(df)


"""Exploratory data analysis """

#groupby 

active=df.groupby(['active_device_id'])
print(active.sum())


#turn data  numerical to be able to aggregate active device pe rorganization or user id 
encoder=LabelEncoder()
active_device=df['active_device_id']=encoder.fit_transform(df['active_device_id'])
print(active_device)

#aggregating active device per organizations and its user_id where is the active device prevalent per org 
operations=['sum','mean']
org_id=df.groupby(['organisation_id', 'user_id'], as_index=False)[['active_device_id']].agg(operations)
print(org_id.reset_index())

#agg per user_id
operations=['sum']
userid=df.groupby(['user_id'], as_index=False)[['active_device_id']].agg(operations)
print(userid.reset_index())


#pivotations to see a bigger picture of the prevalent device id per organization

pivot_org=df.pivot_table(index='organisation_id',columns='organisation_id', aggfunc={'active_device_id':'sum'}).fillna(0)
pivot_org['Max']=pivot_org.idxmax(axis=1)
print(pivot_org)

#

#barchart mean phone defects 
active_id=df.groupby(['organisation_id'])['active_device_id'].mean()
active_id=pd.DataFrame(data=active_id)
active_org_id=active_id.sort_values(by='active_device_id',ascending=False,axis=0)


fig = px.bar(active_org_id, x="active_device_id", y=active_org_id.index, color='active_device_id',color_continuous_scale='Blues',title="Mean of Active Org by active device")
plotly.offline.plot(fig, filename='defects')


active_id=df.groupby(['organisation_id'])['active_device_id'].sum()
active_id=pd.DataFrame(data=active_id)
active_org_id_sum=active_id.sort_values(by='active_device_id',ascending=False,axis=0)

fig = px.bar(active_org_id_sum, x="active_device_id", y=active_org_id_sum.index, color='active_device_id',color_continuous_scale='Blues',title="Sum of Active Org by active device")
plotly.offline.plot(fig, filename='defects')





















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



repairs=pd.read_csv('device_repairs.csv')
print(repairs.columns)
df=DataFrame(repairs)
#print(df)


"""Exploratory data analysis """

#aggregations for all months

operations=['mean','sum','min','max']
all_months=df.groupby(['device_id','repair_cost_currency'], as_index=False)[['repair_cost']].agg(operations)
print(all_months.reset_index())

#agrregations and groupings by days 

#extract February certain day
#2/2/2020
f1=df[df.timestamp_utc=='1/2/2020']
print(f1)
f2=df[df.timestamp_utc=='2/2/2020']
print(f2)
f5=df[df.timestamp_utc=='5/2/2020']
print(f5)
f6=df[df.timestamp_utc=='6/2/2020']
print(f6)
f4=df[df.timestamp_utc=='4/2/2020']
print(f4)
f3=df[df.timestamp_utc=='3/2/2020']
print(f3)
f7=df[df.timestamp_utc=='7/2/2020']
print(f7)
f8=df[df.timestamp_utc=='8/2/2020']
print(f8)
f9=df[df.timestamp_utc=='9/2/2020']
print(f9)
f10=df[df.timestamp_utc=='10/2/2020']
print(f10)
f11=df[df.timestamp_utc=='11/2/2020']
print(f11)
f12=df[df.timestamp_utc=='12/2/2020']
print(f12)

#aggregation for different days of February ex day 10
operations=['mean','sum','min','max']
Feb10=f10.groupby(['device_id','repair_cost_currency'], as_index=False)[['repair_cost']].agg(operations)
print(Feb10.reset_index())

#Feb 2 situation 

Feb2=f2.groupby(['device_id','repair_cost_currency'], as_index=False)[['repair_cost']].agg(operations)
print(Feb2.reset_index())

#PIVOTS on various days

# pivot showing sum of repair cost per device id second day February

pivot1=f2.pivot_table(index='device_id',columns='repair_cost_currency', aggfunc={'repair_cost':'sum'}).fillna(0)
pivot1['Max']=pivot1.idxmax(axis=1)
print(pivot1)

# pivot showing sum of repair cost per device id  day 3  February

pivot1=f3.pivot_table(index='device_id',columns='repair_cost_currency', aggfunc={'repair_cost':'sum'}).fillna(0)
pivot1['Max']=pivot1.idxmax(axis=1)
print(pivot1)

"""Data visualization using PLotly"""


""" 2d Histograms"""
# 2d hiatogram showing distribution of repair cost for Feb 3rd.
fig = px.density_heatmap(f3, x="device_id", y="repair_cost", nbinsx=20, nbinsy=20, color_continuous_scale="Blues_r",title='Repairs Feb 3rd')
plotly.offline.plot(fig, filename='repairs')


#Distribution of currency accross repairs 
fig = px.density_heatmap(df, x="repair_cost_currency", y="repair_cost", nbinsx=20, nbinsy=20, color_continuous_scale="Blues_r",title='Repairs')
plotly.offline.plot(fig, filename='repairs')

"""Heatmaps for correlations"""

#currency and cost correlation for phone repairs

device_id=df['device_id']
repair_cost=df['repair_cost']
repair_cost_currency=df['repair_cost_currency']
timestamp_utc=df['timestamp_utc']

fig = go.Figure(data=go.Heatmap(
                   z=repair_cost,
                   x=repair_cost_currency,
                   y=timestamp_utc,
                   colorscale='Blues'))

fig.update_layout(
    
    title='currency and cost correlation for phone repairs',
    xaxis_nticks=40)

plotly.offline.plot(fig, filename='repairs')

fig = go.Figure(data=go.Heatmap(
                   z=repair_cost,
                   x=device_id,
                   y=timestamp_utc,
                   colorscale='Blues'))

fig.update_layout(
    
    title='currency and cost correlation for phone repairs',
    xaxis_nticks=40)

plotly.offline.plot(fig, filename='repairs')


repair=df.groupby(['device_id'])['repair_cost'].mean()
repair=pd.DataFrame(data=repair)
ph_repair=repair.sort_values(by='repair_cost',ascending=False,axis=0)

fig = px.bar(ph_repair, x="repair_cost", y=ph_repair.index, color='repair_cost',color_continuous_scale='Blues',title="phone repairs")
plotly.offline.plot(fig, filename='repair')

""" sunburst"""

#sunburst per device_id.

fig = px.sunburst(df, path=['device_id','repair_cost_currency'], values='repair_cost',
                  color='repair_cost', hover_data=['repair_cost'],
                  color_continuous_scale='Ice',
                  maxdepth=2,
                  color_continuous_midpoint=np.average(df['repair_cost'], weights=df['repair_cost']))

plotly.offline.plot(fig, filename='repirs') 

fig = px.sunburst(df, path=['device_id','repair_performer_id'], values='repair_cost',
                  color='repair_cost', hover_data=['repair_cost'],
                  color_continuous_scale='Ice',
                  maxdepth=2,
                  color_continuous_midpoint=np.average(df['repair_cost'], weights=df['repair_cost']))

plotly.offline.plot(fig, filename='repirs') 


"""seaborn visualizations"""

#heatmap for feb 10 
plt.figure(figsize=(10,5))
sns.heatmap(f11.corr(),cmap='Blues')
plt.show()

#scatterdots 
vissual2 = sns.lmplot(data=ph_repair, x='repair_cost', y='repair_cost',
                 fit_reg=False)
plt.show()

vissual2 = sns.lmplot(data=df, x='repair_cost_currency', y='repair_cost',
                 fit_reg=False)
plt.show()

#violin chart

sns.violinplot(x=df["repair_cost_currency"], y=df["repair_cost"], palette="Blues")
plt.show()

sns.violinplot(x=df["repair_performer_id"], y=df["repair_cost"], palette="Blues")
plt.show()




















 


 

























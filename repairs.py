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

#extract fbruary certain day
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

#aggregation for different days 
operations=['mean','sum','min','max']
Feb10=f10.groupby(['device_id','repair_cost_currency'], as_index=False)[['repair_cost']].agg(operations)
print(Feb10.reset_index())

Feb2=f2.groupby(['device_id','repair_cost_currency'], as_index=False)[['repair_cost']].agg(operations)
print(Feb2.reset_index())

# pivot showing sum of repair cost per device id second day February

pivot1=f2.pivot_table(index='device_id',columns='repair_cost_currency', aggfunc={'repair_cost':'sum'}).fillna(0)
pivot1['Max']=pivot1.idxmax(axis=1)
print(pivot1)

# pivot showing sum of repair cost per device id  day 3  February

pivot1=f3.pivot_table(index='device_id',columns='repair_cost_currency', aggfunc={'repair_cost':'sum'}).fillna(0)
pivot1['Max']=pivot1.idxmax(axis=1)
print(pivot1)

# 2d hiatogram showing distribution of repair cost for Feb 3rd.
fig = px.density_heatmap(f3, x="device_id", y="repair_cost", nbinsx=20, nbinsy=20, color_continuous_scale="Blues_r",title='Repairs Feb 3rd')
plotly.offline.plot(fig, filename='repairs')


#Distribution of currency accross repairs 
fig = px.density_heatmap(df, x="repair_cost_currency", y="repair_cost", nbinsx=20, nbinsy=20, color_continuous_scale="Blues_r",title='Repairs')
plotly.offline.plot(fig, filename='repairs')








#eda
#corr
#multilinear regression
#vis
 


 



#use py to analyse whatever and make graphs 
#analyze whatever 
#plotly or sns

#it is the last phse of ex which is best create etc. 
#may be us etableau 
























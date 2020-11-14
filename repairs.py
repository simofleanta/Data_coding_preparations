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
print(df)


x_shape=df.shape
print(x_shape)
x_describe=df.describe()
print(x_describe)

#check repaircost sum by timestamp and device_id

operations=['sum','min','max']
a=df.groupby(['timestamp_utc', 'device_id'], as_index=False)[['repair_cost']].agg(operations)
print(a.reset_index())


#extract day 
day2=df[df.timestamp_utc=='2/2/2020']
print(day2)

operations=['sum','min','max']
a=day2.groupby(['timestamp_utc', 'device_id'], as_index=False)[['repair_cost']].agg(operations)
print(a.reset_index())

x=df.groupby(['repair_cost', 'timestamp_utc'])
print(x.sum())

#use py to analyse whatever and make graphs 
#analyze whatever 
#plotly or sns

#it is the last phse of ex which is best create etc. 
























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
x=df.groupby(['organisation_id', 'user_id'], as_index=False)[['active_device_id']].agg(operations)
print(x.reset_index())

#agg per user_id
operations=['sum','mean']
x=df.groupby(['organisation_id', 'user_id'], as_index=False)[['active_device_id']].agg(operations)
print(x.reset_index())








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

#groupby defects for all months

active=df.groupby(['active_device_id'])
print(active.sum())

#turn data  numerical to be able to aggregate active users by organization id 
encoder=LabelEncoder()
org_id=df['organisation_id']=encoder.fit_transform(df['organisation_id'])
print(org_id)





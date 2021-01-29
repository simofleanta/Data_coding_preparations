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
import datetime
import time



#open file
e=pd.read_csv('D202.csv')
print(e.columns)
e_df=DataFrame(e.head(60))
print(e_df.head(60))

#parse index
e_df['DATE']=pd.to_datetime(e_df['DATE'], infer_datetime_format=True)
indexeddf=e_df.set_index(['DATE'])
print(indexeddf)


#parsing to time format and extracting dates with 'created_at'
x=e_df['DATE']=pd.to_datetime(e_df['DATE'], format='%m-%d-%y')

Day=e_df['DATE'].dt.day_name()
Month=e_df['DATE'].dt.month_name()
Year=e_df['DATE'].dt.year

#subsetting timeseries
e_df['Year']=e_df['DATE'].dt.year
e_df['Month']=e_df['DATE'].dt.month
e_df['Day']=e_df['DATE'].dt.day
print(e_df.head(3))


#day_index per week 'D' 
Day_index=indexeddf.resample('D').mean()
print(Day_index)


#weekly index aggregation
Week_index=indexeddf.resample('W').agg({'COST_dollar':'max','USAGE':'max'})












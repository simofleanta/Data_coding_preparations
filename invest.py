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


investing=pd.read_csv('funding.csv')
print(investing.columns)
df=DataFrame(investing.head(5))
#print(df.head(5))

df_invest=df[['created_at','funded_at','raised_amount','raised_amount_usd','is_first_round','is_last_round','funding_round_type','participants']]
print(df_invest.head(4))

df_invest['created_at']=pd.to_datetime(df_invest['created_at'], infer_datetime_format=True)
indexeddf=df_invest.set_index(['created_at'])
print(indexeddf)

#parsing to time format and extracting dates

x=df_invest['created_at']=pd.to_datetime(df_invest['created_at'], format='%y-%m-%d %I-%p')

Day=df_invest['created_at'].dt.day_name()
print(Day)

Month=df_invest['created_at'].dt.month_name()
print(Month)

Year=df_invest['created_at'].dt.year
print(Year)


#subsetting 
df_invest['Year']=df_invest['created_at'].dt.year
df_invest['Month']=df_invest['created_at'].dt.month_name()
df_invest['Day']=df_invest['created_at'].dt.day_name()
print(df_invest.head(4))

#the earliest time for funding 
earliest_time=df_invest['created_at'].min()
print(earliest_time)

#the latest date funded
latest_time=df_invest['created_at'].max()
print(latest_time)

#difference between latest and earliest time funding
diff=latest_time-earliest_time
print(diff)


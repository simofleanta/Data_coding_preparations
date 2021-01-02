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

df_invest=df[['created_at','funded_at','raised_amount','is_first_round','is_last_round','funding_round_type']]
print(df_invest.head(4))

df_invest['created_at']=pd.to_datetime(df_invest['created_at'], infer_datetime_format=True)
indexeddf=df_invest.set_index(['created_at'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'

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

#----------------------------------------------
#date filter

filt=(df_invest['created_at'] >= '2006')
l=df_invest.loc[filt]
print(l)

##############################################################################################

#Datatime indexing and parsing with 'funded_at'

df_invested=df_invest[['funded_at','raised_amount','is_first_round','is_last_round','funding_round_type']]

df_invested['funded_at']=pd.to_datetime(df_invested['funded_at'], infer_datetime_format=True)
indexeddf=df_invested.set_index(['funded_at'])
print(indexeddf)


#parsing to time format and extracting dates with 'created_at'

x=df_invested['funded_at']=pd.to_datetime(df_invested['funded_at'], format='%y-%m-%d')

Day=df_invested['funded_at'].dt.day_name()
print(Day)

Month=df_invested['funded_at'].dt.month_name()
print(Month)

Year=df_invested['funded_at'].dt.year
print(Year)

#subsetting again with the needed columns 

df_invested['Year']=df_invested['funded_at'].dt.year
df_invested['Month']=df_invested['funded_at'].dt.month_name()
df_invested['Day']=df_invested['funded_at'].dt.day_name()
print(df_invested.head(200))






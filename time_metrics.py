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
e=pd.read_csv('metrics3.csv')
#print(e.columns)
e_df=DataFrame(e.head(60))
#print(e_df.head(60))

#parse datetime format for leak_start
e_df['Leak_start']=pd.to_datetime(e_df['Leak_start'], infer_datetime_format=True)
indexeddf=e_df.set_index(['Leak_start'])
#print(indexeddf)


x=e_df['Leak_start']=pd.to_datetime(e_df['Leak_start'], format='%m-%d-%y H:i')

Day=e_df['Leak_start'].dt.day_name()
Month=e_df['Leak_start'].dt.month
Year=e_df['Leak_start'].dt.year
Hour=e_df['Leak_start'].dt.hour
Minute=e_df['Leak_start'].dt.minute


#subsetting timeseries for leak_start 
e_df['Year_start']=e_df['Leak_start'].dt.year
e_df['Month_start']=e_df['Leak_start'].dt.month
e_df['Day_start']=e_df['Leak_start'].dt.day
e_df['Hour_start']=e_df['Leak_start'].dt.hour
e_df['Minute_start']=e_df['Leak_start'].dt.minute
#print(e_df.head(3))



##################################################################

#repeat time procedure for leak_end

e_df['Leak_end']=pd.to_datetime(e_df['Leak_end'], infer_datetime_format=True)
indexeddf=e_df.set_index(['Leak_end'])
#print(indexeddf)

#dt_format for leakend
x=e_df['Leak_end']=pd.to_datetime(e_df['Leak_end'], format='%m-%d-%y H:i')

#setting the series

Day=e_df['Leak_end'].dt.day_name()
Month=e_df['Leak_end'].dt.month
Year=e_df['Leak_end'].dt.year
Hour=e_df['Leak_end'].dt.hour
Minute=e_df['Leak_end'].dt.minute

#subsetting timeseries for leak_end 
e_df['Year_end']=e_df['Leak_end'].dt.year
e_df['Month_end']=e_df['Leak_end'].dt.month
e_df['Day_end']=e_df['Leak_end'].dt.day
e_df['Hour_end']=e_df['Leak_end'].dt.hour
e_df['Minute_end']=e_df['Leak_end'].dt.minute
#print(e_df.head(3))


###########################################################

# dtimes series for Dates

e_df['Dates']=pd.to_datetime(e_df['Dates'], infer_datetime_format=True)
indexeddf=e_df.set_index(['Dates'])
#print(indexeddf)

#dt_format for leakend
x=e_df['Dates']=pd.to_datetime(e_df['Dates'], format='%m-%d-%y H:i')

Year=e_df['Dates'].dt.year
Month=e_df['Dates'].dt.month

#subset dates in year and month

e_df['Year_dates']=e_df['Dates'].dt.year
e_df['Month_dates']=e_df['Dates'].dt.month
print(e_df.head(3))















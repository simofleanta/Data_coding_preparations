
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
import datetime as dt
import time

#ein impfstoff aber, hat keiner Nationalität 

# Supress Scientific notation in python
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Display all columns of long dataframe
pd.set_option('display.max_columns', None)

# open cohort

vax_path='vaccinations.csv'
vax=pd.read_csv(vax_path)
#print(vax)

#parse index
vax['date']=pd.to_datetime(vax['date'], infer_datetime_format=True)
indexeddf=vax.set_index(['date'])
#print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=vax['date']=pd.to_datetime(vax['date'], format='%d-%m-%y')

Day=vax['date'].dt.day_name()
Month=vax['date'].dt.month_name()
Year=vax['date'].dt.year

#subsetting 
vax['Year']=vax['date'].dt.year
vax['Month']=vax['date'].dt.month_name()
vax['Day']=vax['date'].dt.day_name()
print(vax)

##################################

def get_month(x):
    return dt.datetime(x.year,x.month,1)

## Create ClientMonth column
vax['VaxedMonth'] = vax['date'].apply(get_month)

# Group by client_id and select the ClientMonth value
grouping = vax.groupby('iso_code')['VaxedMonth']

## Assign a minimum ClientMonth value to the dataset
vax['VaxedMonth'] = grouping.transform('min')

# calculate time offsets

def get_date_int(df, column):
    year = df[column].dt.year
    month = df[column].dt.month
    return year, month

# Get the integers for date parts from the `ClientMonth` column
vaxed_year, vaxed_month = get_date_int(vax,'VaxedMonth')

# Get the integers for date parts from the `CohortMonth` column
cohort_year, cohort_month = get_date_int(vax,'VaxedMonth')

# Calculate difference in years
years_diff = vaxed_year - cohort_year

# Calculate difference in months
months_diff = vaxed_month - cohort_month

# Extract the difference in months from all previous values
vax['CohortIndex'] = years_diff * 12 + months_diff + 1
print(vax)

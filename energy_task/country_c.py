
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


# Supress Scientific notation in python
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Display all columns of long dataframe
pd.set_option('display.max_columns', None)


# open cohort

country_path='salesc.csv'
scohort=pd.read_csv(country_path)

#parse index
scohort['year']=pd.to_datetime(scohort['year'], infer_datetime_format=True)
indexeddf=scohort.set_index(['year'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=scohort['year']=pd.to_datetime(scohort['year'], format='%d-%m-%y')

Day=scohort['year'].dt.day_name()
Month=scohort['year'].dt.month_name()
Year=scohort['year'].dt.year

#subsetting 
scohort['Year']=scohort['year'].dt.year
scohort['Month']=scohort['year'].dt.month_name()
scohort['Day']=scohort['year'].dt.day_name()

print(scohort)

#############################################

# I ###########parse dates

def get_month(x):
    return dt.datetime(x.year,x.month,1)

## Create ClientMonth column
scohort['ClientMonth'] = scohort['year'].apply(get_month)

# Group by client_id and select the ClientMonth value
grouping = scohort.groupby('Country_code')['ClientMonth']

## Assign a minimum ClientMonth value to the dataset
scohort['CohortMonth'] = grouping.transform('min')

# calculate time offsets

def get_date_int(df, column):
    year = df[column].dt.year
    month = df[column].dt.month
    return year, month

# Get the integers for date parts from the `ClientMonth` column
client_year, client_month = get_date_int(scohort,'ClientMonth')

# Get the integers for date parts from the `CohortMonth` column
cohort_year, cohort_month = get_date_int(scohort,'CohortMonth')


# Calculate difference in years
years_diff = client_year - cohort_year

# Calculate difference in months
months_diff = client_month - cohort_month

# Extract the difference in months from all previous values
scohort['CohortIndex'] = years_diff * 12 + months_diff + 1
print(scohort)



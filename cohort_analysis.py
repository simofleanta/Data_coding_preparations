
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


# open cohort

c=pd.read_csv('cohort.csv')
print(c.columns)
cohort=DataFrame(c.head(62))
print(cohort.head(62))

#parse index
cohort['year']=pd.to_datetime(cohort['year'], infer_datetime_format=True)
indexeddf=cohort.set_index(['year'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=cohort['year']=pd.to_datetime(cohort['year'], format='%d-%m-%y')

Day=cohort['year'].dt.day_name()
Month=cohort['year'].dt.month_name()
Year=cohort['year'].dt.year

#subsetting 
cohort['Year']=cohort['year'].dt.year
cohort['Month']=cohort['year'].dt.month_name()
cohort['Day']=cohort['year'].dt.day_name()

print(cohort)

# I parse dates

def get_month(x):
    return dt.datetime(x.year,x.month,1)

## Create ClientMonth column
cohort['ClientMonth'] = cohort['year'].apply(get_month)

# Group by client_id and select the ClientMonth value
grouping = cohort.groupby('client_id')['ClientMonth']

## Assign a minimum ClientMonth value to the dataset
cohort['CohortMonth'] = grouping.transform('min')

# II 

# calculate time offsets

def get_date_int(df, column):
    year = df[column].dt.year
    month = df[column].dt.month
    return year, month

# Get the integers for date parts from the `ClientMonth` column
client_year, client_month = get_date_int(cohort,'ClientMonth')

# Get the integers for date parts from the `CohortMonth` column
cohort_year, cohort_month = get_date_int(cohort,'CohortMonth')


# III 

# calculate date diff in years

# Calculate difference in years
years_diff = client_year - cohort_year

# Calculate difference in months
months_diff = client_month - cohort_month

# Extract the difference in months from all previous values
cohort['CohortIndex'] = years_diff * 12 + months_diff + 1
#print(cohort)


################IV

#Retention rate
#% of active clients to the total no of clients

#steps:

#1
grouping = cohort.groupby(['CohortMonth', 'CohortIndex'])


#2 count unque vals per clientid

cohort_data = grouping['client_id'].apply(pd.Series.nunique).reset_index()

#step3 create pivot

cohort_counts = cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='client_id')

#step4 Select the first column and store it to cohort_sizes

cohort_sizes = cohort_counts.iloc[:,0]

# step 5 Divide the cohort count by cohort sizes along the rows

retention = cohort_counts.divide(cohort_sizes, axis=0)*100

# V last chunk of the cohort analysis

months=["Jun '6", "Jul '7", "Aug '8", "Sep '9", "Oct '10","Nov '11"]

























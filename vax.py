
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

#create cohort month 
def get_month(x):
    return dt.datetime (x.year, x.month, 1)

vax['VaxedMonth']=vax['date'].apply(get_month)
grouping=vax.groupby('iso_code')['VaxedMonth']
vax['CohortMonth']=grouping.transform('min')


# calculate time offsets

def get_month_int(cohortframe, column):
    year=cohortframe[column].dt.year
    month=cohortframe[column].dt.month
    day=cohortframe[column].dt.day
    return year, month, day


#call function 
vaxed_year, vaxed_month, vaxed_day_=get_month_int(vax,'VaxedMonth')
cohort_year, cohort_month,cohort_day_=get_month_int(vax,'CohortMonth')

#create year an month diffs
year_diff=vaxed_year-cohort_year
month_diff=vaxed_month-cohort_month
day_diff=vaxed_day_ - cohort_day_

#create cohortindex
vax['CohortIndex']=year_diff * 12 + month_diff +1 + day_diff +7

#count monthly active clients from month cohorts

grouping = vax.groupby(['VaxedMonth', 'CohortIndex'])
cohort_data = grouping['iso_code'].apply(pd.Series.nunique)

#return number of unique vals
cohort_data = cohort_data.reset_index()
cohort_counts = cohort_data.pivot(index='VaxedMonth', columns='CohortIndex', values='iso_code')
print(cohort_counts)



#mean quantity on cohorts

grouping = vax.groupby(['VaxedMonth', 'CohortIndex'])
cohort_data = grouping['people_fully_vaccinated'].mean()
cohort_data=cohort_data.reset_index()
avg_q=cohort_data.pivot(index='VaxedMonth', columns='CohortIndex', values='people_fully_vaccinated')
avg_q.round(1)
avg_q.index=avg_q.index.date

plt.figure(figsize=(15,7))
plt.title('people_fully_vaccinated on monthly cohorts')
sns.heatmap(data=avg_q, annot=True, vmin=0.0,  fmt = '.1f', vmax=20, cmap='Blues')
plt.show()




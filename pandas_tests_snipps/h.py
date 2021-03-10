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

c='h.csv'
cohort=pd.read_csv(c, encoding=('ISO-8859-1'), low_memory=False)
#print(cohort.head(5))


#describe data after cleaning nan and duplicated vals
print(cohort.describe())

#print the shape of data
print(cohort.shape)

#parse dates in index (definitely need it)

cohort['Date']=pd.to_datetime(cohort['Date'], infer_datetime_format=True)
indexeddf=cohort.set_index(['Date'])
#print(indexeddf)


################################################based on country code########################################################################

# cohort analysis start

#create cohort month 
def get_month(x):
    return dt.datetime (x.year, x.month, 1)


cohort['ClientMonth']=cohort['Date'].apply(get_month)
grouping=cohort.groupby('Country_code')['ClientMonth']
cohort['CohortMonth']=grouping.transform('min')

print(cohort.tail())


#extract days, months

def get_month_int(cohortframe, column):
    year=cohortframe[column].dt.year
    month=cohortframe[column].dt.month
    day=cohortframe[column].dt.day
    return year, month, day

#call function 
client_year, client_month,_=get_month_int(cohort,'ClientMonth')
cohort_year, cohort_month,_=get_month_int(cohort, 'CohortMonth')

#create year an month diffs
year_diff=client_year - cohort_year
month_diff=client_month - cohort_month

#create cohortindex
cohort['CohortIndex']=year_diff * 12 + month_diff +1

#count monthly active clients from month cohorts

grouping = cohort.groupby(['CohortMonth', 'CohortIndex'])
cohort_data = grouping['Country_code'].apply(pd.Series.nunique)


#return number of unique vals
cohort_data = cohort_data.reset_index()
cohort_counts = cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='Client_Count')
print(cohort_counts)


#build retention table

cohort_size=cohort_counts.iloc[:,0]
retention=cohort_counts.divide(cohort_size, axis=0) 
retention.round(3) *100
print(retention)

plt.figure(figsize=(15,7))
plt.title('Retention levels on monthly cohorts')
sns.heatmap(data=retention, annot=True, linewidth = 1.7 ,fmt='.0%', vmin=0.0, vmax=0.5, cmap='Blues')
plt.show()



grouping = cohort.groupby(['CohortMonth', 'CohortIndex'])
cohort_data = grouping['Out_px'].mean()
cohort_data=cohort_data.reset_index()
avg_q=cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='Out_px')
avg_q.round(2)
avg_q.index=avg_q.index.date

plt.figure(figsize=(15,7))
plt.title('Avg_q on monthly cohorts')
sns.heatmap(data=avg_q, annot=True, fmt='.1f',vmin='0.0', vmax=20, linewidth = 1.7, cmap='viridis')
plt.show()

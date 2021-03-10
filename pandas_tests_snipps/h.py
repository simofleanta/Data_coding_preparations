
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


c='h.csv'
cohort=pd.read_csv(c, encoding=('ISO-8859-1'), low_memory=False)
#print(cohort.head(5))

print(cohort.info())

#describe data after cleaning nan and duplicated vals
print(cohort.describe())

#print the shape of data
print(cohort.shape)

#parse dates in index (definitely need it)

cohort['Date']=pd.to_datetime(cohort['Date'], infer_datetime_format=True)
indexeddf=cohort.set_index(['Date'])
#print(indexeddf)

"""
#parsing to time format and extracting dates with 'created_at'
x=cohort['InvoiceDate']=pd.to_datetime(cohort['InvoiceDate'], format='%y-%m-%d')

Day=cohort['InvoiceDate'].dt.day_name()
Month=cohort['InvoiceDate'].dt.month
Year=cohort['InvoiceDate'].dt.year"""


# cohort analysis start

#create cohort month 
def get_month(x):
    return dt.datetime (x.year, x.month, 1)

cohort['Rate_Month']=cohort['Date'].apply(get_month)
grouping=cohort.groupby('Domain_code')['Rate_Month']
cohort['Rate_Month']=grouping.transform('min')

print(cohort.tail())

#extract days, months

def get_month_int(cohortframe, column):
    year=cohortframe[column].dt.year
    month=cohortframe[column].dt.month
    day=cohortframe[column].dt.day
    return year, month, day
#call function 
invoice_year, invoice_month,_=get_month_int(cohort,'InvoiceMonth')
cohort_year, cohort_month,_=get_month_int(cohort, 'Rate_Month')

#create year an month diffs
year_diff=invoice_year-cohort_year
month_diff=invoice_month-cohort_month

#create cohortindex
cohort['CohortIndex']=year_diff * 12 + month_diff +1

#count monthly active clients from month cohorts

grouping = cohort.groupby(['Rate_Month', 'CohortIndex'])
cohort_data = grouping['Domain_code'].apply(pd.Series.nunique)


#return number of unique vals
cohort_data = cohort_data.reset_index()
cohort_counts = cohort_data.pivot(index='Rate_Month', columns='CohortIndex', values='Domain_code')
print(cohort_counts)


#build retention table

cohort_size=cohort_counts.iloc[:,0]
retention=cohort_counts.divide(cohort_size, axis=0) 
retention.round(3) *100
print(retention)

plt.figure(figsize=(15,7))
plt.title('Retention levels on monthly cohorts')
sns.heatmap(data=retention, annot=True, fmt='.0%', vmin=0.0, vmax=0.5, cmap='Blues')
plt.show()

#mean quantity on cohorts

grouping = cohort.groupby(['Rate_Month', 'CohortIndex'])
cohort_data = grouping['Service_price'].mean()
cohort_data=cohort_data.reset_index()
avg_q=cohort_data.pivot(index='Rate_Month', columns='CohortIndex', values='Service_price')
avg_q.round(1)
avg_q.index=avg_q.index.date

plt.figure(figsize=(15,7))
plt.title('Service_price on monthly cohorts')
sns.heatmap(data=avg_q, annot=True, vmin=0.0, vmax=20, cmap='YlOrRd')
plt.show()

#########################################################################
"""
#mean quantity on cohorts

grouping = cohort.groupby(['CohortMonth', 'CohortIndex'])
cohort_data = grouping['UnitPrice'].mean()
cohort_data=cohort_data.reset_index()
avg_q=cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='UnitPrice')
avg_q.round(1)
avg_q.index=avg_q.index.date

plt.figure(figsize=(15,7))
plt.title('UnitPrice on monthly cohorts')
sns.heatmap(data=avg_q, annot=True, vmin=0.0, vmax=20, cmap='PiYG')
plt.show()"""

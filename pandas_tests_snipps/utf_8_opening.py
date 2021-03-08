
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


c='Online.csv'
cohort=pd.read_csv(c, encoding=('ISO-8859-1'), low_memory=False)
#print(cohort.head(5))

print(cohort.info())

#check in missing data
print(cohort.isnull().sum())

#clean missing data
cohort=cohort.dropna(subset=['CustomerID'])
print(cohort.isnull().sum())

#check for duplicate values and then clean
print(cohort.duplicated().sum())

#clean duplicated
cohort=cohort.drop_duplicates()
print(cohort.duplicated().sum())


#describe data after cleaning nan and duplicated vals
print(cohort.describe())

#print the shape of data
print(cohort.shape)

#parse dates in index (definitely need it)

cohort['InvoiceDate']=pd.to_datetime(cohort['InvoiceDate'], infer_datetime_format=True)
indexeddf=cohort.set_index(['InvoiceDate'])
#print(indexeddf)

"""
#parsing to time format and extracting dates with 'created_at'
x=cohort['InvoiceDate']=pd.to_datetime(cohort['InvoiceDate'], format='%y-%m-%d')

Day=cohort['InvoiceDate'].dt.day_name()
Month=cohort['InvoiceDate'].dt.month
Year=cohort['InvoiceDate'].dt.year"""


# cohort analysis start
def get_month(x):
    return dt.datetime (x.year, x.month, 1)

cohort['InvoiceMonth']=cohort['InvoiceDate'].apply(get_month)
grouping=cohort.groupby('CustomerID')['InvoiceMonth']
cohort['CohortMonth']=grouping.transform('min')

print(cohort.tail())

def get_month_int(cohortframe, column):
    year=cohortframe[column].dt.Year
    month=cohortframe[column].dt.month
    day=cohortframe[column].dt.day
    return year, month, day

























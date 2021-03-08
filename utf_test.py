
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

"""
c='Online.csv'
cohort=pd.read_csv(c, encoding=('ISO-8859-1'), low_memory=False)
print(cohort)


# Supress Scientific notation in python
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Display all columns of long dataframe
pd.set_option('display.max_columns', None)

#parse index
cohort['year']=pd.to_datetime(cohort['year'], infer_datetime_format=True)
indexeddf=cohort.set_index(['year'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=scohort['year']=pd.to_datetime(cohort['year'], format='%d-%m-%y')

Day=cohort['year'].dt.day_name()
Month=cohort['year'].dt.month_name()
Year=cohort['year'].dt.year

#subsetting 
cohort['Year']=cohort['year'].dt.year
cohort['Month']=cohort['year'].dt.month_name()
cohort['Day']=cohort['year'].dt.day_name()

print(cohort)


c='Online.csv'
cohort=pd.read_csv(c, encoding=('ISO-8859-1'), low_memory=False)
print(cohort)"""

e='px.csv'
emps=pd.read_csv(e)
print(emps.head(10))


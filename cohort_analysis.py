
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

# II calculate time offsets















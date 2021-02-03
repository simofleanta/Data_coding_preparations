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

m=pd.read_csv('Actual.csv')
print(m.columns)
m=DataFrame(m.head(10))
print(m.head(10))

#types_of_data
print(m.dtypes)

#parse index
m['Date']=pd.to_datetime(m['Date'], infer_datetime_format=True)
indexeddf=m.set_index(['Date'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=m['Date']=pd.to_datetime(m['Date'], format='%m-%d-%y')

Day=m['Date'].dt.day
Month=m['Date'].dt.month_name()
Year=m['Date'].dt.year

#subsetting 
m['Year']=m['Date'].dt.year
m['Month']=m['Date'].dt.month_name()
m['Day']=m['Date'].dt.day
print(m)

#indexing per month 





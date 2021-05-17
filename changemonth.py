

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
from sklearn.cluster import KMeans
from sklearn.metrics import r2_score
import plotly.express as px
import datetime
import datetime as dt
import time

cmap = sns.diverging_palette(220, 15, as_cmap=True)


# Supress Scientific notation in python
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Display all columns of long dataframe
pd.set_option('display.max_columns', None)


#open file
tlv='editedBRD.csv'
tlv=pd.read_csv(tlv)
print(tlv.head(3))



#parse index
tlv['Date']=pd.to_datetime(tlv['Date'], infer_datetime_format=True)
indexeddf=tlv.set_index(['Date'])
#print(indexeddf)

#parsing to time format and extracting dates 
x=tlv['Date']=pd.to_datetime(tlv['Date'], format='%d-%m-%y')

Day=tlv['Date'].dt.day_name()
Month=tlv['Date'].dt.month_name()
Year=tlv['Date'].dt.year

#subset
tlv['Year']=tlv['Date'].dt.year
tlv['Month']=tlv['Date'].dt.month_name()
tlv['MonthNumber']=tlv['Date'].dt.month
tlv['Day']=tlv['Date'].dt.day
print(tlv.head(3))

df_tlv=tlv.to_csv('TLV.csv')

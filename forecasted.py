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

#forecast_multiply aurorevenue by number of months or days 

f=pd.read_csv('forecasted.csv')
print(f.columns)
f=DataFrame(f.head(21))
print(f.head(21))


f['Date']=pd.to_datetime(f['Date'], infer_datetime_format=True)
indexeddf=f.set_index(['Date'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=f['Date']=pd.to_datetime(f['Date'], format='%m-%d-%y')

Day=f['Date'].dt.day
Month=f['Date'].dt.month_name()
Year=f['Date'].dt.year

#subsetting 
f['Year']=f['Date'].dt.year
f['Month']=f['Date'].dt.month_name()
f['Day']=f['Date'].dt.day
print(f)

#extract months
January=f[f.Month=='January']
February=f[f.Month=='February']

#scatter subplot to see monthly trend and daily trend
f,axes = plt.subplots(1,2, figsize=(15, 10))
Jan=sns.scatterplot(January.Actual_Revenue, January.Forecast_r, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues', ax=axes[0]).set_title("January forecast")

Feb=sns.scatterplot(February.Actual_Revenue, February.Forecast_r, s=100, edgecolor='black', alpha=0.5,\
     palette='viridis',ax=axes[1]).set_title("February forcast")
plt.show()

Month_index=indexeddf.resample('M')
print(Month_index)



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

"""How would we solve a Community problem statement:

Many people live at blocks distance from thei office. It takes them 1 minute per block to the office and around 20 seconds per bloc by bike.
If it takes them various minutes more to walk to office than to ride thaen how many blocks distance do they travel to their offices?

Solutions? """

#open file
bike=pd.read_csv('Bikes_blocks.csv')
print(bike.columns)
bike_df=DataFrame(bike.head(60))
print(bike_df.head(60))

#check dtypes
print(bike_df.dtypes)
# if we hve null values 
print(bike_df.isnull)
#shape of data
print(bike_df.shape)
#data description
print(bike_df.describe())

#parse index
bike_df['year']=pd.to_datetime(bike_df['year'], infer_datetime_format=True)
indexeddf=bike_df.set_index(['year'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=bike_df['year']=pd.to_datetime(bike_df['year'], format='%d-%m-%y')

Day=bike_df['year'].dt.day_name()
Month=bike_df['year'].dt.month_name()
Year=bike_df['year'].dt.year

#subsetting 
bike_df['Year']=bike_df['year'].dt.year
bike_df['Month']=bike_df['year'].dt.month_name()
bike_df['Day']=bike_df['year'].dt.day_name()

print(bike_df.head(3))

#calculate how many blocks can people ride in one minute given their minutes walk?

bike_df['Bike_ride_minute']=60/bike_df.Seconds_per_Block
bike_df['Total_minutes_ride']=bike_df.No_blocks/bike_df.Bike_ride_minute
#finally calculate the difference between minutes walk and ride 
bike_df['Number_blocks_to_office']=bike_df.Min_walk-bike_df.Total_minutes_ride

print(bike_df)




 









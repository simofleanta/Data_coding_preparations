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
from datetime import datetime

repairs=pd.read_csv('device_defects.csv')
print(repairs.columns)
df=DataFrame(repairs)
print(df)



"""Exploratory data analysis """

#groupby defects for all months

defects=df.groupby(['defect_category'])
print(defects.sum())

defect_date=df.groupby(['date'])
print(defect_date.sum())


#turn data  numerical to be able to aggregate phone defect category 
encoder=LabelEncoder()
numerical=df['date']=encoder.fit_transform(df['date'])

#Date mean 50 you get 200 screenbroken defects compared to software defects, 7025 in date mean 58 

operations=['mean','sum','min','max']
defect=df.groupby(['defect_category'], as_index=False)[['date']].agg(operations)
print(defect.reset_index())

defect_date_num=df.groupby(['date','timestamp_utc'])
print(defect_date_num.sum())








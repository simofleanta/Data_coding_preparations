import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
 
#open the file
bikes=pd.read_csv('bikes_h.csv')
print(bikes.columns)
df=DataFrame(bikes)

print(df.head(3))

#extract column
cnt=df['cnt']
print(cnt.head(3))


Registered=df['registered']
Weekday=df['weekday']
Season=df['season']
Hr=df['hr']
Mnth=df['mnth']
Windspeed=df['windspeed']
Yr=df['yr']
Cnt=df['cnt']
Workingday=df['workingday']

h=df.groupby(['weekday'])['cnt'].mean()
hap=pd.DataFrame(data=h)
bike_h=hap.sort_values(by='cnt',ascending=False,axis=0)


fig = px.bar(bike_h, x="cnt", y=bike_h.index, color='cnt',color_continuous_scale='Blues',title="Count bikes/h on weekdays")
plotly.offline.plot(fig, filename='bike')
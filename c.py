#What is the correct mean and standard deviation of the quantity of pasta purchased by time unit by household?

import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
import statistics

#open file
c=pd.read_csv('day.csv')
#print(c.columns)
df=DataFrame(c.head(3))
#print(df.head(10))

#check missing_v
missing_v=df.isnull().sum()
vc=df['cnt'].value_counts()
#print(vc)

#check dtypes before change
types=df.dtypes
#print(types)

#change area in cat
mnth_cat=df.mnth=pd.Categorical(df['mnth'], ordered=True)
#print(mnth_cat)
weekday_cat=df.weekday=pd.Categorical(df['weekday'], ordered=True)
#print(weekday_cat)
#check dtypes after change
types=df.dtypes
#print(types)


m=df.cnt.mean()
#print(m)
n=df.groupby('weekday').cnt.mean()
print(n)
P=df.groupby('mnth').cnt.mean()
#print(P)
P=df.groupby('season').cnt.mean()
#print(P)















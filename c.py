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
c=pd.read_csv('c.csv')
print(c.columns)
df=DataFrame(c.head(3))
print(df.head(50))

#check missing_v
missing_v=df.isnull().sum()
vc=df['TIME'].value_counts()
print(vc)

#check dtypes before change
types=df.dtypes
print(types)

#change area in cat
area_cat=df.AREA=pd.Categorical(df['AREA'], ordered=True)
print(area_cat)
time_cat=df.TIME=pd.Categorical(df['TIME'], ordered=True)
print(time_cat)
#check dtypes after change
types=df.dtypes
print(types)


pasta=df['AREA'].mean()
print(pasta)










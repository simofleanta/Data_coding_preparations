
import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
import statistics
import stats

#What is the correct mean and standard deviation of the quantity of pasta purchased by time unit by household?

c=pd.read_csv('c.csv')
#print(c.columns)
df=DataFrame(c.head(100))
print(df.head(100))

x=df.groupby(['AREA'])[['PASTA']]
print(x.mean())



f=['mean', 'std']
x=df.groupby(['TIME'], as_index=False)[['HHID']].agg(f)
print(x.reset_index())


#What is the average income of households living in area 4?$filter?

paris=df[df.AREA=='Paris'].mean()
print(paris)

paris=df

x=df.groupby(['AREA'])[['INCOME']]
print(x.mean())

#
sums=df.groupby('AREA').INCOME.sum()
print(sums)

means=df.groupby('AREA').INCOME.mean()
print(means)

















































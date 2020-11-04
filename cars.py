
import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
import scipy
import statistics
import stats


c=pd.read_csv('cars_csv.csv')
#print(c.columns)
df=DataFrame(c.head(20))
#print(df.head(10))

#df.describe()
#df.sum()
#df.mean()
df.max()


#Min/max on separate columns
mpg=df.mpg
s=mpg.count()
print(s)

wt=df.wt
f=wt.min()
#print(f)

"""summary stats"""
#df stdev
s=df.std()
#print(s)

mean=df.mean()
#print(mean)

""" Agreggate column"""
d=df.agg(['mean','max','min','var','count'])
#print(d)

"""groupby 2 columns """

g=df.groupby('cyl').mean()
#print(g)
x=df.groupby(['cars_names'])[['cyl']]
#print(x.mean())

# group by with 2 columns and tail(4)
x=df.groupby(['cars_names'], as_index=False)[['carb']].mean().tail(4)
#print(x)

"""aggegate 2 columns"""

f=['mean','max','min','count', 'std','var']
x=df.groupby(['cars_names'], as_index=False)[['carb']].agg(f)
#print(x.reset_index())

x=df[['mpg','hp','wt']]
sns.pairplot(x)
plt.show()

mpg=df['mpg']
hp=df['hp']
qsec=df['qsec']
wt=df['wt']





































import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
g=pd.read_csv('AEP_hourly.csv')
#print(g.columns)
df=DataFrame(g)
print(df.columns)
print(df.head(10))


#no missing_v
missing_v=df.isnull().sum()
print(missing_v)
vc=df['Datetime'].value_counts()

#group AEP_MW by datetime :)
e=df.groupby('Datetime')['AEP_MW'].mean()
print(e.head(5))

df.plot(figsize=(16,4),legend=True)

plt.title('AEP hourly power consumption data - BEFORE NORMALIZATION')

plt.show()

#NORMALIZE DATA BEFORE ANALYSIS 
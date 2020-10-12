import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
#open the file
happy=pd.read_csv('2020.csv')
print(happy.columns)
df=DataFrame(happy)

print(df.head(3))

values=df['Healthy_life_expectancy']
names=df['Regional_indicator']

fig=px.pie(df,
values=values,
names=names,
title='Health_expectancy_regionwise')

fig.update_traces(

textposition='inside',
textinfo='percent + label'
)

fig.show()








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



c=pd.read_csv('bread basket.csv')
print(c.columns)
df=DataFrame(c.head(100))
print(df.head(100))

#groupings
x=df.groupby(['period_day','Item'])[['Transaction']]
#print(x.mean())
y=df.groupby(['Item','weekday_weekend','period_day'])[['Transaction']]
#print(y.mean())

#Aggregate
operations=['mean','sum','min','max']
a=df.groupby(['Item','period_day'], as_index=False)[['Transaction']].agg(operations)
print(a.reset_index())




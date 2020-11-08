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

c=pd.read_csv('heatmap_px.csv')
#print(c.columns)
df=DataFrame(c.head(100))
#print(df.head(100))

x=df.groupby(['yr'])[['px']]
#print(x.mean())

y=df.groupby(['company'])[['px']].mean()
#print(y)

El=df[df.company=='EL']
#print(El)

El=df.groupby(['px']).mean()
#print(El)

#Aggregate
operations=['mean', 'std','sum','min','max']
x=df.groupby(['company'], as_index=False)[['px']].agg(operations)
print(x.reset_index())




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
print(df.head(100))

#corr year px
correlation=df.corr(method='pearson')
#print(correlation)

x=df.groupby(['yr'])[['px']]
#print(x.mean())

y=df.groupby(['company'])[['px']].mean()
#print(y)

El=df[df.company=='EL']
#print(El)

electrica=El.corr(method='pearson')
print(electrica)


El=df.groupby(['px']).mean()
#print(El)

#Aggregate
operations=['mean', 'std','sum','min','max']
sd=df.groupby(['company','yr'], as_index=False)[['px']].agg(operations)
#print(sd.reset_index())


y=df.groupby(['company'])[['px']].mean()
#print(y)


#tables 
import plotly.figure_factory as ff

df=sd

c=df.corr(method='pearson')










import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
import statistics
import plotly.express as px
import stats
import matplotlib.pyplot as plt 


#open the file
cars=pd.read_csv('CarPrice.csv')
print(cars.columns)
df=DataFrame(cars)
print(df.head(100))


#groupings
x=df.groupby(['doornumber'])[['price']]
print(x.mean())
y=df.groupby(['CarName'])[['horsepower']]
print(y.mean())
z=df.groupby(['doornumber','fueltype'])[['horsepower']]
print(z.mean())

#Aggregate
operations=['mean', 'std','sum','min','max']
a=df.groupby(['doornumber','fueltype'], as_index=False)[['price']].agg(operations)
print(a.reset_index())

#corrs
px=df['price']
fueltype=df['fueltype']

px_horse=df[['fueltype','doornumber','price','horsepower']].copy()
correlation=px_horse.corr(method='pearson')
print(correlation)

door_fuel=df[['fueltype','boreratio','horsepower']].copy()
correlation=door_fuel.corr(method='pearson')
print(correlation)


#graphs
sns.violinplot(x=df["fueltype"], y=df["price"], palette="Blues")
#plt.show()

plt.figure(figsize=(10,5))
sns.heatmap(df.corr(),cmap='Blues')
#plt.show()


visual=sns.






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


c=pd.read_csv('bike_business_plan.csv')
#print(c.columns)
df=DataFrame(c.head(100))
#print(df.head(100))

c=df.select_dtypes(object)
#print(c)

#trasnform in numerical
encoder=LabelEncoder()
df['Number_Bikes']=encoder.fit_transform(df['Number_Bikes'])

c=df.dtypes
#print(c)

#groupings
x=df.groupby(['Season'])[['Number_Bikes']]
#print(x.mean())


#Aggregate
operations=['mean','sum','min','max']
a=df.groupby(['Year','Month'], as_index=False)[['Number_Bikes']].agg(operations)
print(a.reset_index())

df['Number_Bikes'].value_counts().sort_values(ascending=False).head(10)

fig, ax=plt.subplots(figsize=(6,4))
df['Month'].value_counts().sort_values(ascending=False).head(10).plot(kind='bar')
plt.ylabel('Number_Bikes')
plt.xlabel('Month')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Best months')


fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
df.groupby('weekday')['Price'].count().sort_values().plot(kind='bar')
plt.ylabel('Price')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Business during the week')




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
import plotly.express as px



c=pd.read_csv('bike_business_plan.csv')
#print(c.columns)
df=DataFrame(c.head(700))
print(df.head(700))

# Numerical
encoder=LabelEncoder()
df['Sales']=encoder.fit_transform(df['Sales'])
df['Number_Bikes']=encoder.fit_transform(df['Number_Bikes'])
df['Item']=encoder.fit_transform(df['Item'])

c=df.select_dtypes(object)
#print(c)

c=df.dtypes
#print(c)

#groupings
x=df.groupby(['Season'])[['Number_Bikes']]
#print(x.mean())

#sort 
df['Number_Bikes'].value_counts().sort_values(ascending=False).head(10)

df.groupby('Month')['Sales'].sum().plot(kind='bar')
plt.ylabel('Sales')
plt.title('Bikes sales in the last months')
plt.show()

#compare 2019-2020
df.groupby('Year')['Sales'].sum().plot(kind='bar')
plt.ylabel('Sales')
plt.title('2019-2020 comparison')
plt.show()

















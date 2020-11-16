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
from datetime import datetime

customers=pd.read_csv('customers.csv')
print(customers.columns)
df=DataFrame(customers)
print(df)

#Customers aggregation to see the relation between customers and best price and to see if customers with longer membership access base prices

operations=['mean','sum','min','max']
customers=df.groupby(['membership_duration_months','pricing_category'], as_index=False)[['base_price']].agg(operations)
print(customers.reset_index())

sns.violinplot(x=df["membership_duration_months"], y=df["base_price"], palette="Blues")
plt.show()

operations=['mean']
customers=df.groupby(['customer_id','pricing_category'], as_index=False)[['base_price']].agg(operations)
print(customers.reset_index())

#pivot  showing that members of 12 mnths access base prices

pivot=df.pivot_table(index='membership_duration_months',columns='membership_duration_months', aggfunc={'base_price':'sum'}).fillna(0)
pivot['Max']=pivot.idxmax(axis=1)
print(pivot)


customers=df.groupby(['membership_duration_months'])['base_price'].mean()
customers=pd.DataFrame(data=customers)
customers_x=customers.sort_values(by='base_price',ascending=False,axis=0)


fig = px.density_heatmap(df, x="membership_duration_months", y="base_price", nbinsx=20, nbinsy=20, color_continuous_scale="Blues_r",title='Membership and base price evolutionl')
plotly.offline.plot(fig, filename='customers')

        
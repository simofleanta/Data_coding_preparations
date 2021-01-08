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

#open file
finance=pd.read_csv('Margin_Analysis.csv')
print(finance.columns)
df_v=DataFrame(finance.head(120))
print(df_v.head(120))

#extract year 2020

"""Year2020=df_v[df_v.Year==2020]
sns.violinplot(x=Year2020["Month"], y=df_v["Sales_Margin"], palette="Blues")

#extract 2019
Year2019=df_v[df_v.Year==2019]
sns.violinplot(x=Year2019["Month"], y=df_v["Sales_Margin"], palette="Blues")


f, axes = plt.subplots(1,2, figsize=(12,6))
k1=sns.violinplot(x=Year2020["Month"], y=df_v["Sales_Margin"], palette="Blues", ax=axes[0])
k2=sns.violinplot(x=Year2019["Month"], y=df_v["Sales_Margin"], palette="Blues", ax=axes[1])
plt.show()"""

#plotly pie
df = px.data.tips()
fig = px.pie(df_v, values='Total_gross_sales', names='Month', color_discrete_sequence=px.colors.sequential.Blues)
plotly.offline.plot(fig, filename='M')

#correlations
plt.figure(figsize=(5,5))
sns.heatmap(df_v.corr(), cmap='Blues')
plt.show()

#implot

vissual1= sns.lmplot(data=df_v, x='Total_gross_sales', y='Gross_Margin',
                 fit_reg=False)
plt.show()










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
import plotly.express as px

#open file
finance=pd.read_csv('Margin_Analysis.csv')
print(finance.columns)
df_v=DataFrame(finance.head(100))
print(df_v.head(10))


finance=pd.read_csv('costs.csv')
print(finance.columns)
df_c=DataFrame(finance.head(100))

#extract year 2020
Year2020=df_v[df_v.Year==2020]

#extract 2019
Year2019=df_v[df_v.Year==2019]
Year2018=df_v[df_v.Year==2018]
Year2017=df_v[df_v.Year==2017]


#visualizing marginal sales and profit in a dashboard junior level
#if there is a plt graph use ax[0,1].scatter  etc. 
#currently there are seaborn stuff

f,axes = plt.subplots(2,2, figsize=(15,30))
K0=sns.scatterplot(df_v.Gross_Margin, df_v.Total_gross_sales, s=100, edgecolor='white', alpha=0.4,\
     palette='Blues',ax=axes[0,0])

k1=sns.stripplot(x='Year', y='Gross_Margin',jitter=0.25, marker='*',alpha=0.6, size=10, linewidth=1, palette="Blues", data=df_v, \
    ax=axes[0,1])

k2=sns.boxplot(df_v.Year, df_v.Sales_Gross, palette='Blues',hue_order=[True,False],ax=axes[1,0])

k3=sns.heatmap(df_v.corr(), annot=True, cmap='Blues',vmin=-1,vmax=1, yticklabels=False, ax=axes[1,1])

plt.show()



#----------------------------------------------------------------------------------------


#polar chart on gross analysis 
df = px.data.wind()

figu = px.scatter_polar(df_v , r="Total_gross_sales", theta="Gross_Margin",symbol='Sales_Gross', template='plotly_dark',
                        color_discrete_sequence=px.colors.sequential.Blues)

plotly.offline.plot(figu, filename='M')






























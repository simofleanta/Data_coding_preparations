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


investing=pd.read_csv('funding.csv')
print(investing.columns)
df=DataFrame(investing.head(200))
print(df.head(200))

df_invest=df[['created_at','object_id','funded_at','post_money_valuation','participants','raised_amount','is_first_round','is_last_round','funding_round_type']]
print(df_invest.head(200))


##############################################################################################

#Datatime indexing and parsing with 'funded_at'

df_invested=df_invest[['funded_at','post_money_valuation','raised_amount','participants','funding_round_type']]

df_invested['funded_at']=pd.to_datetime(df_invested['funded_at'], infer_datetime_format=True)
indexeddf=df_invested.set_index(['funded_at'])
print(indexeddf)


#parsing to time format and extracting dates with 'created_at'

x=df_invested['funded_at']=pd.to_datetime(df_invested['funded_at'], format='%y-%m-%d')

Day=df_invested['funded_at'].dt.day_name()
#print(Day)

Month=df_invested['funded_at'].dt.month_name()
#print(Month)

Year=df_invested['funded_at'].dt.year
#print(Year)

#subsetting again with the needed columns 
df_invested['Year']=df_invested['funded_at'].dt.year
df_invested['Month']=df_invested['funded_at'].dt.month_name()
df_invested['Day']=df_invested['funded_at'].dt.day_name()
#print(df_invested.head(200))

#timeseries filter

filt1=(df_invested['funded_at'] >= '2006')
l1=df_invested.loc[filt1]
#print(l1)

raised=df_invested.groupby(['Year'])[['raised_amount']]
print(raised.sum())

#barchart for amount raised by startuos in years

fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
df_invested.groupby('Year')['raised_amount'].count().sort_values().plot(kind='bar')
plt.ylabel('raised_amount')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('raised_amount in years')
plt.show()

#distribution of amount raised per day 2d histogram 

df = px.data.tips()
fig = px.density_heatmap(df_invested, x="Day", y="raised_amount", nbinsx=40, nbinsy=30, color_continuous_scale="Blues",title='distribution for raised amount per day')
#plotly.offline.plot(fig, filename='i')

#barchart on post money valuation

post_m=df_invested.groupby(['Month'])['post_money_valuation'].mean()
m=pd.DataFrame(data=post_m)
post_money=m.sort_values(by='post_money_valuation',ascending=False,axis=0)
print(post_money)

fig = px.bar(post_money, x="post_money_valuation", y=post_money.index, color='post_money_valuation',color_continuous_scale='Blues',title="Post Money Valuation in months")
plotly.offline.plot(fig, filename='i')

#barchart pot money valuation per year

fig = px.bar(df_invested, x="Year", y=["raised_amount","post_money_valuation"],barmode='stack', color='post_money_valuation',color_continuous_scale='Blues',title="Post money valuation in relation to funding")
plotly.offline.plot(fig, filename='i')
#where there's higher funding there's better valuation, and that happens in 2007

#post vauation in months
fig = px.bar(df_invested, x="Month", y=["raised_amount","post_money_valuation"],barmode='stack', color='post_money_valuation',color_continuous_scale='Blues',title="Post money valuation in relation to funding")
plotly.offline.plot(fig, filename='i')
#where there's higher funding there's better valuation, and that happens at the beginning of the year

#since 2007 is best, we'll filter dive in this year

Year2007=df_invested[df_invested.Year==2007]
print(Year2007)

# month performance 
fig = px.bar(Year2007, x="Month", y=["raised_amount","post_money_valuation"],barmode='stack', color='post_money_valuation',color_continuous_scale='RdBu',title="Post money valuation in relation to funding")
plotly.offline.plot(fig, filename='i')












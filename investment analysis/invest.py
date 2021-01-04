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
plotly.offline.plot(fig, filename='i')

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


# month performance 
fig = px.bar(Year2007, x="funding_round_type", y=["raised_amount","post_money_valuation"],barmode='stack', color='post_money_valuation',color_continuous_scale='RdBu',title="Post money valuation in relation to funding type")
plotly.offline.plot(fig, filename='i')
#series c+ seems highest
#angel investment is in growth

#types of funding analysis 
fig = px.bar(df_invested, x="funding_round_type", y=["raised_amount","post_money_valuation"],barmode='stack', color='post_money_valuation',color_continuous_scale='RdBu',title="Post money valuation in relation to funding type")
plotly.offline.plot(fig, filename='i')
#series c+ seems highest
#angel investment is in growth
#no ventures

#angel investment 
angel=df_invested[df_invested.funding_round_type=='angel']
print(angel)

fig = px.bar(angel, x="Year", y=["raised_amount"],barmode='group', color='participants',color_continuous_scale='RdBu',title="Angel funding in relation to participants")
plotly.offline.plot(fig, filename='i')

#where there are more participants there is more angel funding in 2005

#density map for fundig type 
df = px.data.tips()
fig = px.density_heatmap(df_invested, x="funding_round_type", y="raised_amount", nbinsx=40, nbinsy=30, color_continuous_scale="Blues",title='distribution for raised amount per day')
plotly.offline.plot(fig, filename='i')

# some correlations
plt.figure(figsize=(10,10))
plt.title('Correlation between funding type and amount raised', y=1.05, size=15)
sns.heatmap(df_invested.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='Blues', linecolor='white', annot=True)
plt.show()

#Relationship between funding type and raised amount
pairplot = sns.pairplot(df_invested, vars=['raised_amount','funding_round_type'])
plt.show()

#regplots on tpes of funding
fig = px.scatter(df_invested, x="raised_amount", y="post_money_valuation", color="funding_round_type", opacity=0.5,trendline="lowess")
plotly.offline.plot(fig, filename='i')

#regplot on 2007
fig = px.scatter(Year2007, x="raised_amount", y="post_money_valuation", color="funding_round_type", opacity=0.5,trendline="lowess")
plotly.offline.plot(fig, filename='i')

# Conclusions 
#2007 is best
#Post money valuation is goes hand in had with raised amount as there is higher valuation where the amount raised is high
#worth looking at the economic context to see level of funding attraction
#best amounts raised from series A+ followed by Angel
#there is a weak correlation between post money valuation and ramount rasised 
#the relationship between funding type and raised amounts shows which type of funding is more accessible. Series B and angel.
#where there is lower amounts raised for other types of funding, there's less acess for ex. ventures and others. 
#regplots show that types of funding reveal not only the type of company but also the amount of money companies can usually raiseusing the types of funding. 
#worth checking domain of topic and type company 















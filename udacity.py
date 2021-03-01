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
import datetime

"""In my Udacity Data Science Challenge, I was supposed to practice Python and create some data visuals using pandas data frames, with data. The aim of 
the exercise was to go through basic data types, data frames and juggling with the data so obtain a small data analysis on random data

So this ex will go through:
opening file
checking data types and making sense of the data
date timeseries parsing
one or 2 carts 
subplots 

Insights I'm looking for:

* What products sell best
* In which place Products sell best
* Possible correlations

"""

#open file
u=pd.read_csv('udacity.csv')
print(u.columns)
udacity=DataFrame(u.head(60))
print(udacity.head(60))

#check dtypes
print(udacity.dtypes)
# if we hve null values 
print(udacity.isnull)
#shape of data
print(udacity.shape)
#data description
print(udacity.describe())

#parse index
udacity['year']=pd.to_datetime(udacity['year'], infer_datetime_format=True)
indexeddf=udacity.set_index(['year'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=udacity['year']=pd.to_datetime(udacity['year'], format='%d-%m-%y')

Day=udacity['year'].dt.day_name()
Month=udacity['year'].dt.month_name()
Year=udacity['year'].dt.year

#subsetting 
udacity['Year']=udacity['year'].dt.year
udacity['Month']=udacity['year'].dt.month_name()
udacity['Day']=udacity['year'].dt.day_name()


"""Analyzing data using Python  Seaborn charts"""

#subplot 
f,axes = plt.subplots(1,2, figsize=(15, 10))
fig1=sns.violinplot(x=udacity["Products"], y=udacity["Profit"], palette="summer",ax=axes[0])
fig2=sns.boxplot(udacity.Place, udacity.Profit, palette='viridis',hue_order=[True,False],ax=axes[1])


#scatter subplot
f,axes = plt.subplots(1,2, figsize=(15, 10))
A=sns.scatterplot(udacity.Out_px, udacity.Profit, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0])

B=sns.scatterplot(udacity.Margin, udacity.Profit, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[1])



#correlation map
sns.heatmap(udacity.corr(), annot=True, cmap='Blues', linewidth=1,vmin=-1,vmax=1, yticklabels=True,xticklabels=True)


"""Conclusions"""

#Laptops sell best
#they sell best in EU
#there are many correlations according to the heatmap


#######################################################

print(udacity)

# open cohort

c=pd.read_csv('cohort.csv')
print(c.columns)
cohort=DataFrame(c.head(1113))
print(cohort.head(1113))

#apply groupby for curiosity
x=cohort.groupby(['client_id', 'Day'])[['Profit']]
print(x.sum())

# I

#define f to parse date
def get_day(x):
    return datetime.datetime(x.year,x.day,1) 

#create column client_Day
cohort['Client_Day'] = cohort['year'].apply(get_day)

#Group by clientid and select the InvoiceMonth value
grouping = cohort.groupby('client_id')['Client_Day'] 



# II 

# Assign a minimum Clien_Day value to the dataset
cohort['CohortDay'] = grouping.transform('min')

def get_date_int(df, column):
    year = df[column].dt.year
    month = df[column].dt.month
    Day=df[column].dt.day
    return year, month,Day


# Get the integers for date parts from the `InvoiceMonth` column
client_year, client_month, client_day = get_date_int(cohort,'Client_Day')

# Get the integers for date parts from the `CohortMonth` column
cohort_year, cohort_month, cohort_day= get_date_int(cohort,'CohortDay')

# III

# Calculate difference in years
years_diff = client_year - cohort_year

# Calculate difference in months
months_diff = client_year - cohort_month

# Calculate difference in days
day_diff = client_day - cohort_day

# Extract the difference in months from all previous values
cohort['CohortIndex'] = day_diff * 30 + months_diff + 1

#IV

grouping = cohort.groupby(['cohort_month', 'CohortIndex'])

















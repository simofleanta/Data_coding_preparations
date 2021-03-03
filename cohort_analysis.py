
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
import datetime as dt
import time

# Supress Scientific notation in python
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Display all columns of long dataframe
pd.set_option('display.max_columns', None)


# open cohort

c=pd.read_csv('cohort.csv')
print(c.columns)
cohort=DataFrame(c.head(152))
print(cohort.head(152))

#parse index
cohort['year']=pd.to_datetime(cohort['year'], infer_datetime_format=True)
indexeddf=cohort.set_index(['year'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=cohort['year']=pd.to_datetime(cohort['year'], format='%d-%m-%y')

Day=cohort['year'].dt.day_name()
Month=cohort['year'].dt.month_name()
Year=cohort['year'].dt.year

#subsetting 
cohort['Year']=cohort['year'].dt.year
cohort['Month']=cohort['year'].dt.month_name()
cohort['Day']=cohort['year'].dt.day_name()

print(cohort)


# I ###########parse dates

def get_month(x):
    return dt.datetime(x.year,x.month,1)

## Create ClientMonth column
cohort['ClientMonth'] = cohort['year'].apply(get_month)

# Group by client_id and select the ClientMonth value
grouping = cohort.groupby('client_id')['ClientMonth']

## Assign a minimum ClientMonth value to the dataset
cohort['CohortMonth'] = grouping.transform('min')

# ###############II 

# calculate time offsets

def get_date_int(df, column):
    year = df[column].dt.year
    month = df[column].dt.month
    return year, month

# Get the integers for date parts from the `ClientMonth` column
client_year, client_month = get_date_int(cohort,'ClientMonth')

# Get the integers for date parts from the `CohortMonth` column
cohort_year, cohort_month = get_date_int(cohort,'CohortMonth')


############ III 

# calculate date diff in years

# Calculate difference in years
years_diff = client_year - cohort_year

# Calculate difference in months
months_diff = client_month - cohort_month

# Extract the difference in months from all previous values
cohort['CohortIndex'] = years_diff * 12 + months_diff + 7
print(cohort)


################IV

#Retention rate
#% of active clients to the total no of clients

#steps:

#1
grouping = cohort.groupby(['CohortMonth', 'CohortIndex'])


#2 count unque vals per clientid

cohort_data = grouping['client_id'].apply(pd.Series.nunique).reset_index()

#step3 create pivot

cohort_counts = cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='client_id')

#step4 Select the first column and store it to cohort_sizes

cohort_sizes = cohort_counts.iloc[:,0]

# step 5 Divide the cohort count by cohort sizes along the rows

retention = cohort_counts.divide(cohort_sizes, axis=0)*100

# V last chunk of the cohort analysis

months=["Jun '18", "Jul '18", "Aug '18", \
        "Sep '19", "Oct '19","Nov '19",\
            "Dec '19", "Jan '20", "Feb '20", "Mar '20", "Apr '20",\
                "May '20", "Jun '20"]

# setup inches plot figure
plt.figure(figsize=(15,7))

# title- clients cohots
plt.title('Retention by Monthly client_Cohorts')


# Create the heatmap
sns.heatmap(data=retention,
            annot = True,
            cmap = "Blues",
            vmin = 0.0,
            #volmax = 0.5,
            vmax = list(retention.max().sort_values(ascending = False))[1]+3,
            fmt = '.1f',
            linewidth = 0.3,
            yticklabels=months)

plt.show()
#####################################################################3


#avg px/cohort 



# Create a groupby object and pass the monthly cohort and cohort index as a list
groupings = cohort.groupby(['CohortMonth', 'CohortIndex']) 

# Calculate the average of the unit price column
cohort_datas = grouping['Out_px'].mean()

# Reset the index of cohort_data
cohort_datas = cohort_datas.reset_index()

# Create a pivot 
average_price = cohort_datas.pivot(index='CohortMonth', columns='CohortIndex', values='Out_px')
average_price.round(2)
average_price.index = average_price.index.date


month_list=["Jun '18", "Jul '18", "Aug '18", \
        "Sep '19", "Oct '19","Nov '19",\
            "Dec '19", "Jan '20", "Feb '20", "Mar '20", "Apr '20",\
                "May '20", "Jun '20"]

# Add a title
plt.title('Average price by Monthly Cohorts')

# Create the heatmap
sns.heatmap(data = average_price,
            annot=True,
            vmin = 20,
#             vmax =20,
            cmap='Blues',
            vmax = list(average_price.max().sort_values(ascending = False))[1]+3,
            fmt = '.1f',
            linewidth = 0.7,
            yticklabels=month_list)
plt.show()

########################################


#avg profit/cohort 


# Create a groupby object and pass the monthly cohort and cohort index as a list
groupings = cohort.groupby(['CohortMonth', 'CohortIndex']) 

# Calculate the average of the unit price column
cohort_datas = grouping['Profit'].mean()

# Reset the index of cohort_data
cohort_datas = cohort_datas.reset_index()

# Create a pivot 
average_profit = cohort_datas.pivot(index='CohortMonth', columns='CohortIndex', values='Profit')
average_profit.round(2)
average_profit.index = average_profit.index.date


month_list=["Jun '18", "Jul '18", "Aug '18", \
        "Sep '18", "Oct '19","Nov '19",\
            "Dec '19", "Jan '20", "Feb '20", "Mar '20", "Apr '20",\
                "May '20", "Jun '20"]

# Add a title
plt.title('Average profit by Monthly Cohorts')

# Create the heatmap
sns.heatmap(data = average_profit,
            annot=True,
            vmin = 20,
#             vmax =20,
            cmap='Blues',
            vmax = list(average_profit.max().sort_values(ascending = False))[1]+8,
            fmt = '.1f',
            linewidth = 0.7,
            yticklabels=month_list)
plt.show()

######################################3

# country code distribution by month cohorts
cohort_datas = grouping['Country_code'].max()

# Reset the index of cohort_data
cohort_datas = cohort_datas.reset_index()

# Create a pivot 
Country_code = cohort_datas.pivot(index='CohortMonth', columns='CohortIndex', values='Country_code')
Country_code.round(5)
Country_code.index = Country_code.index.date
plt.figure(figsize=(15,7))

month_list=["Jun '18", "Jul '18", "Aug '18", \
        "Sep '19", "Oct '19","Nov '19",\
            "Dec '19", "Jan '20", "Feb '20", "Mar '20", "Apr '20",\
                "May '20", "Jun '20"]

# Add a title
plt.title('Country_Code distribution by Monthly Cohorts')

# Create the heatmap
sns.heatmap(data = Country_code,
            annot=True,
            vmin = 20,
#             vmax =20,
            cmap='YlOrRd',
            vmax = list(Country_code.max().sort_values(ascending = False))[1]+3,
            fmt = '.1f',
            linewidth = 0.7,
            yticklabels=month_list)
plt.show()





























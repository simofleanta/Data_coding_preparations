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

"""How would we solve a Community problem statement:

Many people live at blocks distance from thei office. It takes them 1 minute per block to the office and around 20 seconds per bloc by bike.
If it takes them various minutes more to walk to office than to ride thaen how many blocks distance do they travel to their offices?

Solutions? """

#open file
bike=pd.read_csv('Bikes_blocks.csv')
print(bike.columns)
bike_df=DataFrame(bike.head(60))
print(bike_df.head(60))

#check dtypes
print(bike_df.dtypes)
# if we hve null values 
print(bike_df.isnull)
#shape of data
print(bike_df.shape)
#data description
print(bike_df.describe())

#parse index
bike_df['year']=pd.to_datetime(bike_df['year'], infer_datetime_format=True)
indexeddf=bike_df.set_index(['year'])
print(indexeddf)

#parsing to time format and extracting dates with 'created_at'
x=bike_df['year']=pd.to_datetime(bike_df['year'], format='%d-%m-%y')

Day=bike_df['year'].dt.day_name()
Month=bike_df['year'].dt.month_name()
Year=bike_df['year'].dt.year

#subsetting timeseries
bike_df['Year']=bike_df['year'].dt.year
bike_df['Month']=bike_df['year'].dt.month_name()
bike_df['Day']=bike_df['year'].dt.day_name()
print(bike_df.head(3))

#-----------------------------

#calculations

#1 what is the number of blocks people walk to their office 
#2 as it takes a couple of minutes more thatn on the bike, people walk 1 minute per block and ride more blocks in 60 seconds 
#3 which leads to the fifference between number of blocks and the actual ride mintes 

#How many blocks can people ride in 60 seconds  given their minutes walk?
bike_df['Blocks_ride_minute']=60/bike_df.Seconds_per_Block

#What is the total minutes ride?
bike_df['Total_minutes_ride']=bike_df.No_blocks/bike_df.Blocks_ride_minute

#finally what is the difference between number of blocks and  minutes on byke to office ?
bike_df['Number_blocks_to_office']=bike_df.No_blocks-bike_df.Total_minutes_ride

#print desired columns for visuals
bikes_office=bike_df[['Year','Month','Day','Min_walk','No_blocks','Seconds_per_Block','Blocks_ride_minute','Total_minutes_ride','Number_blocks_to_office']].copy()
print(bikes_office)


#--------------------------------------------------

# PLots


#How far the people travel to their work?
f,axes = plt.subplots(1,2, figsize=(15, 10))
A=sns.scatterplot(bikes_office.Min_walk, bikes_office.Number_blocks_to_office, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0])

B=sns.scatterplot(bikes_office.Total_minutes_ride, bikes_office.Number_blocks_to_office, s=100, edgecolor='black', alpha=0.5,\
     palette='viridis',ax=axes[1])

plt.show()


#Filter for Thursday  

bike_day=bikes_office[bikes_office.Day=='Thursday']
bike_Wed=bikes_office[bikes_office.Day=='Wednesday']

#Day benchmark 

#Which day is more frequently on th bike?

f,axes = plt.subplots(1,2, figsize=(15, 10))
Thursday=sns.scatterplot(bike_day.Min_walk, bike_day.Total_minutes_ride, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0])

Wednesday=sns.scatterplot(bike_Wed.Min_walk, bike_Wed.Total_minutes_ride, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[1])

plt.show()

#Which day is more frequently on th bike?

f,axes = plt.subplots(1,2, figsize=(15, 10))
C=sns.scatterplot(bike_day.Min_walk, bike_day.Total_minutes_ride, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0])

D=sns.boxplot(bikes_office.Day, bikes_office.Total_minutes_ride, palette='viridis',hue_order=[True,False],ax=axes[1])

plt.show()

#--------------------------------------

#SPEED ON LANES

#if cyclists increase speed to their work by 30% and then by 10% what % of  speed of the original ride would be their total increase?
# we need to find the total % increase
#dearting from the initial ride value increase other 30.then increase by 10% whock gives the final speed increase. calculate final speed as %.


bike_speed=bike_df[['Year','Month','Day','Total_minutes_ride','Number_blocks_to_office','Ride_speed']].copy()
print(bike_speed)

bike_speed['First_Increase']=bike_speed.Ride_speed * 0.3
bike_speed['Increase2']=bike_speed.First_Increase*0.1
bike_speed['All_Speed_Increase']=bike_speed.Increase2+bike_speed.First_Increase
bike_speed['Final_Speed_As_p']=bike_speed.Ride_speed*43/100
print(bike_speed)

#plotting consumption patterns before app 
f,axes = plt.subplots(2,2, figsize=(15,30))
K0=sns.scatterplot(bike_speed.Total_minutes_ride, bike_speed.Final_Speed_As_p, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0,0])

k1=sns.stripplot(x='Day', y='Final_Speed_As_p',jitter=0.25, marker='*',alpha=0.6, size=10, linewidth=1, palette="Blues", data=bike_speed, \
    ax=axes[0,1])

k2=sns.boxplot(bike_speed.Day, bike_speed.Final_Speed_As_p, palette='Blues',hue_order=[True,False],ax=axes[1,0])

k3=sns.scatterplot(bike_speed.Number_blocks_to_office, bike_speed.Final_Speed_As_p, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues', ax=axes[1,1])

plt.show()


#Conclusions 

#The problem understanding is as such:
#1 what is the number of blocks people walk to their office 
#2 as it takes a couple of minutes more thatn on the bike, people walk 1 minute per block and ride more blocks in 60 seconds 
#3 which leads to the fifference between number of blocks and the actual ride mintes 

#charts showing how far are people from their work

#People are between 10-24 minutes away of their work but is matters more how they rech it. 
#It is clear that riding the bike halfs the time to get to work because in les seconds riding the bike covers more blocks thatn walking
#Charts show that while some get to work in 18 minutes walking, bike riders do it in 12 minutes 
#Thursday has the highest bike minutes than any other day in the week. 

#Sucggestions

#Since we're talking about neighbourhood and relatively small distances:
#draw map shortcuts and encourage people to use those shortcuts, including those who prefer walking 
#build bike parks (rent, parking bikes etc.)


















 









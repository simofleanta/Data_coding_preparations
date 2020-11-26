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

"""A friend has a bike business and wants to see the business evolution given the pandemic situ
if 2019 is better than 2020
he would like to see what bikes sell best?
what are the best months and days?"""

#EDA-gropings, sortings, mean, max, sum values in aggregs 
#pivotations
#visuals with seaborn
#visuals with plotly (also a separate section containing plotly)
#function on roi 
#a/b approach 
#Weather context 
#economics  
#profitability 

c=pd.read_csv('bike_business_plan.csv')
print(c.columns)
df=DataFrame(c.head(500))
print(df.head(500))

#subset - to combine columns in a df showing an ex of sales on very good weather 
#merge!= combine 
year_2019=df[df.Year==2019]
year_2020=df[df.Year==2020]
combined_col=year_2019[4:8][['Month','Item','Sales','weather_forecast']]
#print(combined_col)

#stack df merge on certain columns 
m=year_2019.append(year_2020)
#print(m)
combine_m=m[10:-40][['Month','Year','Item','Sales','weather_forecast']]
print(combine_m)

#second day benchmark per year 2019,2020
day2_2019=year_2019[year_2019.Day==2]
day2_2020=year_2020[year_2020.Day==2]
stack=day2_2019.append(day2_2020)
day_stack=stack[2:10][['Year','Month','Item','weather_forecast','Sales']]
print(day_stack)




#concat - horrizontally 
conc=pd.concat([year_2020,year_2019])
#print(conc)

#pd merge good if one df has only 2/3 columns compred t the orther
merged=pd.merge(year_2019,year_2020)
#print(merged.columns)





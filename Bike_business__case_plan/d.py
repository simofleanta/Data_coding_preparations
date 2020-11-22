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
what are the best months and days?
What is the ROI"""

#EDA-gropings, sortings, mean, max, sum values in aggregs 
#pivotations
#visuals with seaborn
#visuals with plotly (also a separate section containing plotly)
#function on roi 



c=pd.read_csv('bike_business_plan.csv')
#print(c.columns)
df=DataFrame(c.head(500))
#print(df.head(500))

a=df['Interested']
b=df['Likely']
c=df['Not_interested']
d=df['Not_likely']


#subset add calculation to dataset
#add df['a]=forumula
df['A']=df.Interested/df.Likely
df['B']=df.Not_interested/df.Not_likely
print(df.columns)

#print dataset with the situations A,B
print(df.head (3))

#aggregate ABs 

Season_A=df.groupby(['Season','Item'])[['A']]
print(Season_A.mean())

Season_B=df.groupby(['Season','Item'])[['B']]
print(Season_B.mean())















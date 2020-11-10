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


#open the file
cars=pd.read_csv('CarPrice.csv')
print(cars.columns)
df=DataFrame(cars)
#print(df.head(100))

a=df.shape
print(a)
b=df.dtypes
#print(b)

#turn in numerical 

c=df.select_dtypes(object)
#print(c)

# there are 10 object type columns in data we will convert this to numberical using LabelEncoder
encoder=LabelEncoder()
df['CarName']=encoder.fit_transform(df['CarName'])
df['fueltype']=encoder.fit_transform(df['fueltype'])
df['aspiration']=encoder.fit_transform(df['aspiration'])
df['doornumber']=encoder.fit_transform(df['doornumber'])
df['carbody']=encoder.fit_transform(df['carbody'])
df['drivewheel']=encoder.fit_transform(df['drivewheel'])
df['enginelocation']=encoder.fit_transform(df['enginelocation'])
df['enginetype']=encoder.fit_transform(df['enginetype'])
df['cylindernumber']=encoder.fit_transform(df['cylindernumber'])
df['fuelsystem']=encoder.fit_transform(df['fuelsystem'])

c=df.dtypes
#print(c)

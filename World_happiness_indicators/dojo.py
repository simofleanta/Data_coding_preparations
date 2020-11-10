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

from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
data['CarName']=encoder.fit_transform(df['CarName'])
data['fueltype']=encoder.fit_transform(df['fueltype'])
data['aspiration']=encoder.fit_transform(df['aspiration'])
data['doornumber']=encoder.fit_transform(df['doornumber'])
data['carbody']=encoder.fit_transform(df['carbody'])
data['drivewheel']=encoder.fit_transform(df['drivewheel'])
data['enginelocation']=encoder.fit_transform(df['enginelocation'])
data['enginetype']=encoder.fit_transform(df['enginetype'])
data['cylindernumber']=encoder.fit_transform(df['cylindernumber'])
data['fuelsystem']=encoder.fit_transform(df['fuelsystem'])

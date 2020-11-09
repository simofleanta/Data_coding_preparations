import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
import statistics
import stats


#open the file
cars=pd.read_csv('CarPrice.csv')
print(cars.columns)
df=DataFrame(cars)
print(df.head(100))

x=df.groupby(['doornumber'])[['price']]
print(x.mean())
y=df.groupby(['CarName'])[['horsepower']]
print(y.mean())


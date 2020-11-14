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
import calendar
import time
from datetime import datetime
import datetime


repairs=pd.read_csv('device_repairs.csv')
print(repairs.columns)
df=DataFrame(repairs)
print(df)


x_shape=df.shape
print(x_shape)
x_describe=df.describe()
#print(x_describe)

ty=type(df.timestamp_utc)
print(ty)

x=df.index
print(x)



operations=['sum','min','max']
a=df.groupby(['timestamp_utc'], as_index=False)[['repair_cost']].agg(operations)
print(a.reset_index())


















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

c=pd.read_csv('bike_business_plan.csv')
print(c.columns)
df=DataFrame(c.head(500))
print(df.head(500))


#roi 
investment=40000 #received investment 
bike_costs=Item_cost_month=df['Item_cost_month']
loss=Loss_item=df['Loss_item']
net_profit=bike_costs*12-loss

df['roi']=net_profit/investment*100
print(df.tail(5))














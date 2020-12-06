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


"""ROI ON 2020 in a pandemic it was anticipated a larger use of echo transport including bikes 
instead of public transport so the investment was higher"""

investment=40000 #received investment 
bike_costs=Item_cost_month=df['Item_cost_month']
loss=Loss_item=df['Loss_item']

net_profit=bike_costs*12-loss
def ROI(investment,bike_costs,loss):
    return net_profit/investment*100


"""def roi(investment,bike_costs,loss):
    net_prof=bike_costs*12-loss
    roi=(net_prof/investment*100)
    return roi

ROI=roi(investment,bike_costs,loss)
print(ROI)

#on 2019
investment=40000
bike_costs=1000
loss=700

def roi(investment,bike_costs,loss):
    net_prof=bike_costs*12-loss
    roi=(net_prof/investment*100)
    return roi

ROI=roi(investment,bike_costs,loss)
print(ROI)"""
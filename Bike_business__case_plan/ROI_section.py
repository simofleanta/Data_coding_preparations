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
bike_costs=Sales=df['Sales']
loss=Number_bikes=df['Number_Bikes']

def roi(bike_costs,loss):
    return bike_costs*12-loss

print(roi(bike_costs,loss))







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
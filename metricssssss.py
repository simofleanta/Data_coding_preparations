import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import statistics
import stats
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import plotly.express as px
import datetime
import time


""" Processing time series on domestic Electric energy consumption"""

#open file
e=pd.read_csv('D202.csv')
print(e.columns)
e_df=DataFrame(e)
print(e_df)
#normalize data
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


#open file
finance=pd.read_csv('Margin_Analysis.csv')
print(finance.columns)
df_v=DataFrame(finance.head(100))
print(df_v.head(10))

#normalize
dataf=df_v[['Year','Sales_Margin','Total_gross_sales', 'Sales_Gross','Gross_Margin']]
dataf=dataf.apply (lambda x: (x-x.min(axis=0)) / (x.max(axis=0) - x.min(axis=0)))
print(dataf)
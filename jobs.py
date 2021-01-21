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
import datetime

jobs=pd.read_csv('BusinessAnalyst1.csv')
print(jobs.columns)
BA=DataFrame(jobs.head(60))
print(BA.head(60))



f,axes = plt.subplots(2,2, figsize=(15,30))
K0=sns.scatterplot(BA.Size, BA.Rating, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0,0])

k1=sns.violinplot(x=BA["Type_ownership"], y=BA["Salary_Estimate_k"], palette="Blues", ax=axes[0,1])

k2=sns.violinplot(x=BA["Salary_Estimate_k"], y=BA["Founding_Year"], palette="Blues",ax=axes[1,0])

k3=sns.violinplot(x=BA["Size"], y=BA["Type_ownership"], palette="Blues", ax=axes[1,1])

plt.show()




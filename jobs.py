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
BA=DataFrame(jobs.head(600))
print(BA.head(600))



# difference between ba, bi, da

business_analyst=BA[BA.Job_Title=='Business Analyst']
print(business_analyst)

business_intelligence=BA[BA.Job_Title=='Business_Intelligence_Analyst']
print(business_intelligence)

data_analyst=BA[BA.Job_Title=='Data Analyst']
print(data_analyst)


#subplot intelligence

f,axes = plt.subplots(1,2, figsize=(15, 10))
C=sns.scatterplot(business_intelligence.Salary_Estimate_k, business_intelligence.Rating, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0])

D=sns.boxplot(business_intelligence.Salary_Estimate_k, business_intelligence.Sector, palette='viridis',hue_order=[True,False],ax=axes[1])

plt.show()

#subplot Business analyst

f,axes = plt.subplots(1,2, figsize=(15, 10))
C=sns.scatterplot(business_analyst.Salary_Estimate_k, business_analyst.Rating, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0])

D=sns.boxplot(business_analyst.Salary_Estimate_k, business_analyst.Sector, palette='viridis',hue_order=[True,False],ax=axes[1])

plt.show()

#subplot data analyst

f,axes = plt.subplots(1,2, figsize=(15, 10))
C=sns.scatterplot(data_analyst.Salary_Estimate_k, data_analyst.Rating, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0])

D=sns.boxplot(data_analyst.Salary_Estimate_k, data_analyst.Sector, palette='viridis',hue_order=[True,False],ax=axes[1])

plt.show()















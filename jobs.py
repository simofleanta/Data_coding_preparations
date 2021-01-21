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



# ba study

business_analyst=BA[BA.Job_Title=='Business Analyst']
print(business_analyst)

business_intelligence=BA[BA.Job_Title=='Business_Intelligence_Analyst']
print(business_intelligence)
"""
f,axes = plt.subplots(1,2, figsize=(15, 10))
C=sns.scatterplot(business_intelligence.Salary_Estimate_k, business_intelligence.Rating, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0])

D=sns.boxplot(business_intelligence.Salary_Estimate_k, business_intelligence.Sector, palette='viridis',hue_order=[True,False],ax=axes[1])

plt.show()"""

#sub2

f,axes = plt.subplots(1,2, figsize=(15, 10))
C=sns.scatterplot(business_analyst.Salary_Estimate_k, business_analyst.Rating, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0])

D=sns.boxplot(business_analyst.Salary_Estimate_k, business_analyst.Sector, palette='viridis',hue_order=[True,False],ax=axes[1])

plt.show()





"""
f,axes = plt.subplots(2,2, figsize=(9,9))
K0=sns.scatterplot(business_intelligence.Salary_Estimate_k, business_intelligence.Rating, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0,0])

k1=sns.scatterplot(business_analyst.Salary_Estimate_k, business_analyst.Rating, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues', ax=axes[0,1])

k2=sns.boxplot(business_intelligence.Salary_Estimate_k, business_intelligence.Sector, palette='viridis',hue_order=[True,False],ax=axes[1,0])

k3=sns.violinplot(x=business_analyst["Size"], y=business_analyst["Type_ownership"], palette="Blues", ax=axes[1,1])

plt.show()"""

















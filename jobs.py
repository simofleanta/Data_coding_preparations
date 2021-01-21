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
K0=sns.stripplot(x='Rating', y='Type_ownership',jitter=0.25, marker='*',alpha=0.6, size=10, linewidth=1, palette="Blues", data=BA,ax=axes[0,0])

k1=sns.violinplot(x=BA["Salary_Estimate_k"], y=BA["Type_ownership"], palette="Blues", ax=axes[0,1])

k2=sns.violinplot(x=BA["Salary_Estimate_k"], y=BA["Founding_Year"], palette="Blues",ax=axes[1,0])

k3=sns.violinplot(x=BA["Size"], y=BA["Type_ownership"], palette="Blues", ax=axes[1,1])

plt.show()

# ba study

business_analyst=BA[BA.Job_Title=='Business Analyst']
print(business_analyst)

f,axes = plt.subplots(2,2, figsize=(9,17))
K0=sns.stripplot(x='Rating', y='Sector',jitter=0.25, marker='*',alpha=0.6, size=10, linewidth=1, palette="Blues", data=business_analyst,ax=axes[0,0])

k1=sns.violinplot(x=business_analyst["Salary_Estimate_k"], y=business_analyst["Type_ownership"], palette="Blues", ax=axes[0,1])

k2=sns.violinplot(x=business_analyst["Salary_Estimate_k"], y=business_analyst["Sector"], palette="Blues",ax=axes[1,0])

k3=sns.violinplot(x=business_analyst["Size"], y=business_analyst["Type_ownership"], palette="Blues", ax=axes[1,1])

plt.show()

# subplot on ba 

f,axes = plt.subplots(1,2, figsize=(15, 10))
C=sns.stripplot(x='Rating', y='Sector',jitter=0.25, marker='*',alpha=0.6, size=10, linewidth=1, palette="Blues", data=business_analyst,ax=axes[0])

D=sns.stripplot(x='Salary_Estimate_k', y='Sector',jitter=0.25, marker='*',alpha=0.6, size=10, linewidth=1, palette="Blues", data=business_analyst,ax=axes[1])
plt.show()








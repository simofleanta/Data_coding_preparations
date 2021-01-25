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

#open file
j=pd.read_csv('joined_t.csv')
print(j.columns)
ba=DataFrame(j.head(21))
print(ba.head(21))

#scatter subplot
f,axes = plt.subplots(1,2, figsize=(15, 10))
A=sns.scatterplot(ba.Salary, ba.KPI, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0])

B=fig2=sns.boxplot(ba.Location, ba.KPI, palette='viridis',hue_order=[True,False], ax=axes[1])

plt.show()


sns.heatmap(ba.corr(), annot=True, cmap='Blues', linewidth=1,vmin=-1,vmax=1, yticklabels=True,xticklabels=True)
plt.show()










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

avg=pd.read_csv('ba avg jobs rate.csv')
print(avg.columns)
ba_avg=DataFrame(avg.head(15))
print(ba_avg.head(15))


# rating and average salary


#subplot 

f,axes = plt.subplots(1,2, figsize=(15, 10))
C=sns.scatterplot(ba_avg.Rating, ba_avg.Salary_K, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0]).set_title("Relationship Avg.Salary and Rating")

D=sns.boxplot(ba_avg.Salary_K, ba_avg.Sector, palette='viridis',hue_order=[True,False],ax=axes[1]).set_title("Avg.Salary per Sector")

plt.show()

sns.heatmap(ba_avg.corr(), annot=True, cmap='Blues', linewidth=1,vmin=-1,vmax=1, yticklabels=True,xticklabels=False)
plt.show()













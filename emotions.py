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
import time

e=pd.read_csv('Focus_data.csv')
print(e.columns)
e_df=DataFrame(e.head(1500))


#emotions corrs
sns.heatmap(e_df.corr(), annot=True, cmap='Blues', linewidth=1,vmin=-1,vmax=1, yticklabels=True,xticklabels=True)
plt.show()

#anger sad & happy-engagement relationships

#copy df
em=e_df[['person_id','happy','sadness','engagement','anger']].copy()

#subplot emtions 

f,axes = plt.subplots(1,2, figsize=(15, 10))
A=sns.scatterplot(em.sadness, em.anger, s=100, edgecolor='black', alpha=0.5,\
     palette='viridis',ax=axes[0])

B=sns.scatterplot(em.engagement, em.happy, s=100, edgecolor='black', alpha=0.5,\
     palette='viridis',ax=axes[1])

plt.show()








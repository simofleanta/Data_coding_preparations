import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
h=pd.read_csv('2015.csv')
print(h.columns)
df=DataFrame(h)

print(df.head(3))

#create a mini dataset from where to take desired columns to create corrs through heatmaps
generosity=df[['Generosity','Family','Happiness Rank']].copy()
freedom=df[['Freedom','Happiness Score','Generosity']].copy()

heat1=generosity.corr()
plt.figure(figsize=(10,6))
sns.heatmap(heat1,annot=True, cmap='RdPu')
plt.show()

heat2=generosity.corr()
plt.figure(figsize=(10,6))
sns.heatmap(heat1,annot=True, cmap='Blues')
plt.show()

plt.figure(figsize=(10,6))
sns.pairplot(heat1)
plt.show()








import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
 
#open the file
bikes=pd.read_csv('bikes_h.csv')
print(bikes.columns)
df=DataFrame(bikes)

print(df.head(3))

#violin
sns.violinplot(x=df["workingday"], y=df["cnt"], palette="Blues")
plt.show()

sns.violinplot(x=df["weekday"], y=df["cnt"], palette="Blues")
plt.show()


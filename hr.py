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

hr=pd.read_csv('hr.csv')
print(hr.columns)
df=DataFrame(hr.head(113))
print(df.head(113))


encoder=LabelEncoder()
df['interview_call']=encoder.fit_transform(df['interview_call'])


sns.violinplot(x=df["Type job"], y=df["interview_call"], palette="Blues")
plt.show()



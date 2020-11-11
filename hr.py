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
numeric=df['interview_call']=encoder.fit_transform(df['interview_call'])
print(numeric)

# more jobs applied for seem graduate 
sns.violinplot(x=df["Job_seniority"], y=df["interview_call"], palette="Blues")

sns.violinplot(x=df["region"], y=df["interview_call"], palette="Blues")


x=df.groupby(['Job_seniority'])[['interview_call']]
print(x.mean())

#aggregation 
operations=['mean','sum','min','max']
a=df.groupby(['Job_seniority','Domain'], as_index=False)[['interview_call']].agg(operations)
print(a.reset_index())






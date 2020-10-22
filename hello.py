import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
g=pd.read_csv('2017_german_election_party.csv')
#print(g.columns)
df=DataFrame(g)

#check dtypes
types=df.dtypes
#print(types)
#no missing_v
missing_v=df.isnull().sum()
#print(missing_v)
vc=df['party'].value_counts()
#print(vc)

#rename columns model
#de=df.rename(columns={'x.Name':'y_Name'},inplace=True)
#df.head()

d=df.groupby(['party'])['votes_first_vote'].sum().sort_values(ascending =False)[:5]
print(d)
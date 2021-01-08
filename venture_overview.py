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

#open file
finance=pd.read_csv('Margin_Analysis.csv')
print(finance.columns)
df_v=DataFrame(finance.head(120))
print(df_v.head(120))

#extract year 2020

Year2020=df_v[df_v.Year==2020]
sns.violinplot(x=Year2020["Month"], y=df_v["Sales_Margin"], palette="Blues")
plt.show()


#extract 2019
Year2019=df_v[df_v.Year==2019]
sns.violinplot(x=Year2019["Month"], y=df_v["Sales_Margin"], palette="Blues")
plt.show()










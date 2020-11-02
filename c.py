#What is the correct mean and standard deviation of the quantity of pasta purchased by time unit by household?

import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly

c=pd.read_csv('c.csv')
print(c.columns)
df=DataFrame(c.head(3))
print(df)

#no missing_v
missing_v=df.isnull().sum()
vc=df['TIME'].value_counts()
print(vc)






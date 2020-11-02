#What is the correct mean and standard deviation of the quantity of pasta purchased by time unit by household?

import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
import statistics
import stats


c=pd.read_csv('cars_csv.csv')
#print(c.columns)
df=DataFrame(c.head(3))
print(df.head(10))

df.describe()
df.sum()















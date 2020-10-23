import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
g=pd.read_csv('AEP_hourly.csv')
#print(g.columns)
df=DataFrame(g)
print(df.columns)
print(df.head(10))
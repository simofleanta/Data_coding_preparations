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

c=pd.read_csv('c.csv')
#print(c.columns)
df=DataFrame(c.head(100))
print(df.head(100))


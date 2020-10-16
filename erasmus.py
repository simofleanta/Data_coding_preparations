import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly

#open the file
s=pd.read_csv('Erasmus_mobility.csv')
print(s.columns)
df=DataFrame(s)

print(df.head(3))
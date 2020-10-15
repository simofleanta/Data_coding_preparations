import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
c=pd.read_csv('covid_de.csv')
print(c.columns)
df=DataFrame(c)

print(df.head(3))


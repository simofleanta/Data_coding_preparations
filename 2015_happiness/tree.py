import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly


#open the file
h=pd.read_csv('2015.csv')
print(h.columns)
df=DataFrame(h)

print(df.head(3))

freedom2=df[['Freedom','Trust (Government Corruption)','Economy (GDP per Capita)','Happiness Rank']].copy()
print(freedom2)

freedom=freedom2['Freedom']
trust=freedom2['Trust (Government Corruption)']
gdp=freedom2['Economy (GDP per Capita)']
rank=freedom2['Happiness Rank']


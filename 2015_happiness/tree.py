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

freedom2=df[['Freedom','Region','Trust (Government Corruption)','Economy (GDP per Capita)','Happiness Rank']].copy()


freedom=freedom2['Freedom']
trust=freedom2['Trust (Government Corruption)']
gdp=freedom2['Economy (GDP per Capita)']
rank=freedom2['Happiness Rank']
Region=freedom2['Region']



region_gdp=freedom2.groupby(['Region'])['Economy (GDP per Capita)'].mean()
gdp_r=pd.DataFrame(data=region_gdp)
gdp_region=gdp_r.sort_values(by='Economy (GDP per Capita)',ascending=False,axis=0)
print(gdp_region)

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


#groupping by country in WE Region-barchart
WE=df[df.Region =='Western Europe']
Country=WE['Country']
print(WE)

WE_fam=WE.groupby(['Country'])['Family'].mean()
WE_fam=pd.DataFrame(data=WE_fam)
Family_c=WE_fam.sort_values(by='Family',ascending=False,axis=0)
print(Family_c)

fig = px.bar(Family_c, x="Family", y=Family_c.index, color='Family',color_continuous_scale='Blues',title="Family on regions")

plotly.offline.plot(fig, filename='hap')
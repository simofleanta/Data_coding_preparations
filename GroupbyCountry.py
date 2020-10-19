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


#Family barchart in WE
"""WE=df[df.Region =='Western Europe']
Country=WE['Country']
print(WE)

WE_fam=WE.groupby(['Country'])['Family'].mean()
WE_fam=pd.DataFrame(data=WE_fam)
Family_c=WE_fam.sort_values(by='Family',ascending=False,axis=0)
print(Family_c)

fig = px.bar(Family_c, x="Family", y=Family_c.index, color='Family',color_continuous_scale='Blues',title="Family on regions")
plotly.offline.plot(fig, filename='hap')"""

#Family barchart in CE

"""CE=df[df.Region =='Central and Eastern Europe']
Country=CE['Country']
print(CE)

CE_fam=CE.groupby(['Country'])['Family'].mean()
CE_fam=pd.DataFrame(data=CE_fam)
Family_central=CE_fam.sort_values(by='Family',ascending=False,axis=0)
print(Family_central)

fig = px.bar(Family_central, x="Family", y=Family_central.index, color='Family',color_continuous_scale='Blues',title="Family in the Central Eastern")
plotly.offline.plot(fig, filename='hap')"""

#Australia and New Zealand family

AZ=df[df.Region =='Australia and New Zealand']
Country=AZ['Country']
print(AZ)

AZ_fam=AZ.groupby(['Country'])['Family'].mean()
AZ_fam=pd.DataFrame(data=AZ_fam)
Family_az=AZ_fam.sort_values(by='Family',ascending=False,axis=0)
print(Family_az)

fig = px.bar(Family_az, x="Family", y=Family_az.index, color='Family',color_continuous_scale='Blues',title="Family in the Australia NZ")
plotly.offline.plot(fig, filename='hap')







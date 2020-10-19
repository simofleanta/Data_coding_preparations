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

#Australia and New Zealand GDP

"""AZ=df[df.Region =='Australia and New Zealand']
Country=AZ['Country']


AZ_gdp=AZ.groupby(['Country'])['Economy (GDP per Capita)'].mean()
AZ_gdp=pd.DataFrame(data=AZ_gdp)
gdp_az=AZ_gdp.sort_values(by='Economy (GDP per Capita)',ascending=False,axis=0)
print(gdp_az)

fig = px.bar(gdp_az, x="Economy (GDP per Capita)", y=gdp_az.index, color='Economy (GDP per Capita)',color_continuous_scale='Blues',title="Family in the Australia NZ")
plotly.offline.plot(fig, filename='hap')"""

#WE GDP GROUPBY

WE=df[df.Region =='Western Europe']
Country=WE['Country']

WE_gdp=WE.groupby(['Country'])['Economy (GDP per Capita)'].mean()
WE_gdp=pd.DataFrame(data=WE_gdp)
gdp_c=WE_gdp.sort_values(by='Economy (GDP per Capita)',ascending=False,axis=0)
print(gdp_c)

fig = px.bar(gdp_c, x="Economy (GDP per Capita)", y=gdp_c.index, color='Economy (GDP per Capita)',color_continuous_scale='Blues',title="GDP mean in different countries")
plotly.offline.plot(fig, filename='hap')














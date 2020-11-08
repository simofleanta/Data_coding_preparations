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

c=pd.read_csv('heatmap_px.csv')
#print(c.columns)
df=DataFrame(c.head(100))
print(df.head(100))

#corr year px
correlation=df.corr(method='pearson')
#print(correlation)

"""Groupings and agg"""

x=df.groupby(['yr'])[['px']]
#print(x.mean())

y=df.groupby(['company'])[['px']].mean()
#print(y)

El=df.groupby(['px']).mean()
#print(El)

y=df.groupby(['company'])[['px']].mean()
#print(y)

#Aggregate
operations=['mean', 'std','sum','min','max']
sd=df.groupby(['company','yr'], as_index=False)[['px']].agg(operations)
#print(sd.reset_index())


"""correlations Pearson for companies"""

El=df[df.company=='EL']
brd=df[df.company=='BRD']
snp=df[df.company=='SNP']
sng=df[df.company=='SNG']
tlv=df[df.company=='TLV']
year=df['yr']
company=df['company']

ELec=El.corr(method='pearson')
brd_generale=brd.corr(method='pearson')
Snp=snp.corr(method='pearson')
Sng=sng.corr(method='pearson')
Tlv=tlv.corr(method='pearson')
#print(ELec)
#print(brd_generale)
#print(Snp)
#print(Sng)
#print(Tlv)
sns.pairplot(ELec)
plt.show()



















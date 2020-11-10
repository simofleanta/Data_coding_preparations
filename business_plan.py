import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import numpy as np
import plotly
import statistics
import plotly.express as px
import stats
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


c=pd.read_csv('bike_business_plan.csv')
#print(c.columns)
df=DataFrame(c.head(700))
#print(df.head(700))

c=df.select_dtypes(object)
#print(c)

#trasnform in numerical
encoder=LabelEncoder()
df['Number_Bikes']=encoder.fit_transform(df['Number_Bikes'])

c=df.dtypes
#print(c)

#groupings
x=df.groupby(['Season'])[['Number_Bikes']]
#print(x.mean())


#Aggregate
operations=['mean','sum','min','max']
a=df.groupby(['Year','Month'], as_index=False)[['Number_Bikes']].agg(operations)
print(a.reset_index())

df['Number_Bikes'].value_counts().sort_values(ascending=False).head(10)



#when is the bike business doing the tbest  during the day. 

fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
df.groupby('Day_Time')['Item'].count().sort_values().plot(kind='bar')
plt.ylabel('Number_Bikes')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Business during the day')
plt.show()


sortbyday=df.groupby('Day_Time')['Item'].count().sort_values(ascending=False)

#business in the past months

df.groupby('Item')['Month'].count().plot(kind='bar')
plt.ylabel('Number_Bikess')
plt.title('Bikes number during the past months')
plt.show()

#extract month situation
Okt=df.loc[df['Month']=='Okt'].nunique()


#pivots. I should add the bike brand name so I can see which one is the pivot one
pivot1=df.pivot_table(index='Season',columns='Item', aggfunc={'Number_Bikes':'count'}).fillna(0)
pivot1['Max']=pivot1.idxmax(axis=1)
print(pivot1)

df.groupby('Item')['weekday'].count().plot(kind='bar')
plt.ylabel('Price')
plt.title('Bikes prices in the last days')
plt.show()

pivot2=df.pivot_table(index='Season',columns='Item', aggfunc={'Price':'count'}).fillna(0)
pivot2['Max']=pivot2.idxmax(axis=1)
print(pivot2)

#corr
plt.figure(figsize=(15,15))
sns.heatmap(df.corr(),annot=True,cmap='Blues_r',mask=np.triu(df.corr(),k=1))
plt.show()

#Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, 
# GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, 
# Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, 
# RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, 
# Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r,
#  autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r,
#  copper,
#  copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, 
# gist_ncar_r, # gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, 
# gray, gray_r, hot, hot_r,#  hsv, hsv_r, icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako, 
# mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r,
#  rocket, rocket_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, 
# tab20c, tab20c_r, terrain, terrain_r, twilight, 
# twilight_r, twilight_shifted, twilight_shifted_r, viridis, viridis_r, vlag, vlag_r, winter, winter_




















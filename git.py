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
import ast
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import plotly.express as px

#pening a file
git=pd.read_csv('GitHub_data.csv')
#print(git.columns)
df=DataFrame(git.head(1000))
#print(df.head(20))

#data view
c=df.dtypes
c_missing=df.isnull().sum()
#print(c_missing)
x=c.describe()
#print(x)
x_describe=df.describe()
#print(x_describe)
x_shape=df.shape
#print(x_shape)

#just in case need to encode numerical 
#encoder=LabelEncoder()
#numerical=df['date']=encoder.fit_transform(df['date'])

#index rename
df = df.rename(columns={'Unnamed: 0': 'index', 'Unnamed: 0.1': 'sub_index'})
df.drop('index', axis=1, inplace=True)
df.reset_index(drop=True, inplace=True)

info=df.info()
print(info)
print(df.columns)

#get rid of str 5000+
x=df.at[700, 'issue'] = str(5000)

#get rid of commas making columns numerical
Numerical = ["star","watch","issue","pull_requests","projects","commits","branches","packages","releases","contributers"]
df[Numerical] = df[Numerical].fillna(0)
df["issue"] = df["issue"].apply(lambda x: x.replace(',', '') if ',' in x else x).astype(float)
df["pull_requests"] = df["pull_requests"].apply(lambda x: x.replace(',', '') if ',' in x else x).astype(float)
df["commits"] = df["commits"].apply(lambda x: x.replace(',', '') if ',' in x else x).astype(float)
df["branches"] = df["branches"].apply(lambda x: x.replace(',', '') if ',' in x else x).astype(float)
df["contributers"] = df["contributers"].apply(lambda x: x.replace(',', '') if ',' in x else x).astype(float)
df["fork"] = df["fork"].apply(lambda x: x.replace(',', '') if ',' in x else x).astype(float)

#Making sense of data

xdf=df[['topic','projects','contributers','name','user','pull_requests','star','fork','issue','License','commits']].copy()
print(xdf)

#how many projects are per topic?
git_topic=xdf.groupby(['topic'])[['projects']]
print(git_topic.count())

#how many projects in total?
proj_count=xdf.groupby(['projects'])
print(proj_count.count())

#how many contribs per topic?
git_contribs=xdf.groupby(['topic'])[['contributers']]
print(git_contribs.count())

#how many contribs in projects
contribs_projects=xdf.groupby(['topic','projects'])[['contributers']]
print(contribs_projects.count())

git_star=xdf.groupby(['projects'])[['star']]
print(git_star.mean())

git_name_star=xdf.groupby(['topic','name'])[['star']]
print(git_name_star.sum())


git_license=xdf.groupby(['topic','License'])[['fork']]
print(git_license.sum())

#barcharts

#projects
fig1 = px.bar(xdf, x="topic", y=["projects"],barmode='group', color='topic',color_continuous_scale='Blues',title="Projects per topic")
#plotly.offline.plot(fig1, filename='git')

fig = px.bar(xdf, x="topic", y=["fork"],barmode='group', color='topic',color_continuous_scale='Blues',title="Forks on topics")
#plotly.offline.plot(fig, filename='git')

#stars
git_d=df.groupby(['topic'])['star'].mean()
days=pd.DataFrame(data=git_d)
git_bar=days.sort_values(by='star',ascending=False,axis=0)

fig = px.bar(git_bar, x="star", y=git_bar.index, color='star',color_continuous_scale='Blues',title="Stars per topic")
#plotly.offline.plot(fig, filename='git')

#pulls
git_d=df.groupby(['topic'])['pull_requests'].mean()
pull=pd.DataFrame(data=git_d)
git_pulls=pull.sort_values(by='pull_requests',ascending=False,axis=0)

fig = px.bar(git_pulls, x="pull_requests", y=git_bar.index, color='pull_requests',color_continuous_scale='Blues',title="Pull requests per topic")
#plotly.offline.plot(fig, filename='git')

fig = px.bar(xdf, x="topic", y=["fork","star"],barmode='stack', color='fork',color_continuous_scale='Blues',title="Star per topic with forks stacked on topics")
#plotly.offline.plot(fig, filename='git')

#fork distribution accross the topics 
df['fork'] = df['fork'].astype(float)
fork_topicwise = df.groupby('topic').sum()['fork']
fig = px.bar(fork_topicwise,x=fork_topicwise.index,y="fork",color=fork_topicwise.index)
plotly.offline.plot(fig, filename='git')


#now that we can see the stars according to the topic, let's see the corr between star& fork
#heatmap corr between star & fork

c=xdf[['star','fork','topic','projects','pull_requests']].copy()

plt.figure(figsize=(8,5))
sns.heatmap(c.corr(),cmap='Blues')
plt.show()

#-star& fork=1.0 most correlated
#pull_request &projects=0.6


































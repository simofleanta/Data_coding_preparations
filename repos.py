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
Numerical = ["star","watch","fork","issue","pull_requests","projects","commits","branches","releases","contributers"]
df[Numerical] = df[Numerical].fillna(0)
df["issue"] = df["issue"].apply(lambda x: x.replace(',', '') if ',' in x else x).astype(float)
df["pull_requests"] = df["pull_requests"].apply(lambda x: x.replace(',', '') if ',' in x else x).astype(float)
df["commits"] = df["commits"].apply(lambda x: x.replace(',', '') if ',' in x else x).astype(float)
df["branches"] = df["branches"].apply(lambda x: x.replace(',', '') if ',' in x else x).astype(float)
df["contributers"] = df["contributers"].apply(lambda x: x.replace(',', '') if ',' in x else x).astype(float)
df["fork"] = df["fork"].apply(lambda x: x.replace(',', '') if ',' in x else x).astype(float)

#Making sense of data

xdf=df[['topic','watch','projects','contributers','name','user','pull_requests','star','fork','issue','License','commits']].copy()
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

#------distributions------

#fork distribution accross the topics 
df['fork'] = df['fork'].astype(float)
fork_topicwise = df.groupby('topic').sum()['fork']
fig = px.bar(fork_topicwise,x=fork_topicwise.index,y="fork",color=fork_topicwise.index)
#plotly.offline.plot(fig, filename='git')

#pull distribution accross the topics 
df['pull_requests'] = df['pull_requests'].astype(float)
pull_topicwise = df.groupby('topic').sum()['pull_requests']
fig = px.bar(pull_topicwise,x=pull_topicwise.index,y="pull_requests",color=pull_topicwise.index)
#plotly.offline.plot(fig, filename='git')

#star distribution accross the topics 
df['star'] = df['star'].astype(float)
star_topicwise = df.groupby('topic').sum()['star']
fig = px.bar(star_topicwise,x=star_topicwise.index,y="star",color=star_topicwise.index)
#plotly.offline.plot(fig, filename='git')

#scatters

fig = px.scatter(xdf, x="topic", y="star", color="fork",
                 size='fork', hover_data=['fork'],
                 color_continuous_scale='Blues',
                 title='star-fork')
#plotly.offline.plot(fig, filename='git')

fig = px.scatter(xdf, x="topic", y="watch", color="issue",
                 size='issue', hover_data=['issue'],
                 color_continuous_scale='RdBu',
                 title='Watching and issues per topic')
#plotly.offline.plot(fig, filename='git')

fig = px.scatter(xdf, x="topic", y="watch", color="commits",
                 size='commits', hover_data=['commits'],
                 color_continuous_scale='RdBu',
                 title='Commits and watching per topic')
#plotly.offline.plot(fig, filename='git')

fig = px.scatter(xdf, x="topic", y="commits", color="pull_requests",
                 size='pull_requests', hover_data=['pull_requests'],
                 color_continuous_scale='Magma',
                 title='Commits and pull_requests per topic')
#plotly.offline.plot(fig, filename='git')


#-----correlations------------------------

#heatmap corr between star & fork

c=xdf[['star','fork','topic','projects','pull_requests','watch','issue','License','commits']].copy()

#numerical corrs
plt.figure(figsize=(10,10))
plt.title('Star-fork corr', y=1.05, size=15)
sns.heatmap(df[Numerical].corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='Blues', linecolor='white', annot=True)

#corrs
plt.figure(figsize=(10,5))
sns.heatmap(c.corr(),annot=True,cmap='Greens')
#plt.show()

#-star& fork=not corr
#pull_request &projects=0.29
#commits -issue-0.66

#-------------Heatmaps

#since star fork strongy corrrelated, we'll do a heatmap 
topic=xdf['topic']
star=xdf['star']
fork=xdf['fork']
issue=xdf['issue']
pull=xdf['pull_requests']
projects=xdf['projects']
commits=xdf['commits']
user=xdf['user']
name=xdf['name']

fig = go.Figure(data=go.Heatmap(
                   z=star,
                   x=fork,
                   y=topic,
                   colorscale='Blues'))

fig.update_layout(
    
    title='stat-fork heatmap',
    xaxis_nticks=40)
#plotly.offline.plot(fig, filename='git')

#--------------------2d histograms

df = px.data.tips()
fig = px.density_heatmap(xdf, x="topic", y="fork", nbinsx=40, nbinsy=30, color_continuous_scale="Viridis",title='star distribution accross the topics')
#plotly.offline.plot(fig, filename='git')

df = px.data.tips()
fig = px.density_heatmap(xdf, x="topic", y="star", nbinsx=40, nbinsy=30, color_continuous_scale="Viridis",title='Star distribution accross the topics')
#plotly.offline.plot(fig, filename='git')

df = px.data.tips()
fig = px.density_heatmap(xdf, x="topic", y="commits", nbinsx=40, nbinsy=30, color_continuous_scale="Viridis",title='Commits distribution')
#plotly.offline.plot(fig, filename='git')

df = px.data.tips()
fig = px.density_heatmap(xdf, x="topic", y="watch", nbinsx=40, nbinsy=30, color_continuous_scale="Viridis",title='watching repos')
#plotly.offline.plot(fig, filename='git')

df = px.data.tips()
fig = px.density_heatmap(xdf, x="topic", y="issue", nbinsx=40, nbinsy=30, color_continuous_scale="Viridis",title='issue repos')
#plotly.offline.plot(fig, filename='git')

#license

df = px.data.tips()
fig = px.density_heatmap(xdf, x="License", y="watch", nbinsx=40, nbinsy=30, color_continuous_scale="Viridis",title='watching repos')
#plotly.offline.plot(fig, filename='git')

df = px.data.tips()
fig = px.density_heatmap(xdf, x=["License"], y="fork", nbinsx=40, nbinsy=30, color_continuous_scale="Viridis",title='watching repos')
#plotly.offline.plot(fig, filename='git')

#to draw conclusions on the above charts

"""Time to filter stuff :) """

#It seems a surprise that data science is not so active on my the charts. So let's see its star-fork behaviours

Data_science=xdf[xdf.topic=='Data-Science']
ml=xdf[xdf.topic=='ML']
print(Data_science)
print(ml)

#corrs
plt.figure(figsize=(6,5))
sns.heatmap(Data_science.corr(),annot=True,cmap='magma')


#starfork not corr
#strongest corr btween projects and pull requests  
#commits-issue=0.47

#Machine learning 

m=xdf[xdf.topic=='ML']
plt.figure(figsize=(10,10))
plt.title('Star-fork corr', y=1.05, size=15)
sns.heatmap(m.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='viridis', linecolor='white', annot=True)


#in ml star-fork is corr=0.27
#strongest one is 
#issue pull requests
#issue commits

comm_stack=ml.append(Data_science)
com=comm_stack[:400][['topic','commits','fork']]
print(com)

vissual2 = sns.lmplot(data=com, x='fork', y='commits',
                 fit_reg=False)
plt.show()









































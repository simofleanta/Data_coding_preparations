
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
import plotly.express as px
import datetime
import datetime as dt
import time


c='transactions.csv'
cohort=pd.read_csv(c, encoding=('ISO-8859-1'), low_memory=False)
#print(cohort.head(5))

print(cohort.info())

#check in missing data
print(cohort.isnull().sum())

#clean missing data
cohort=cohort.dropna(subset=['ID'])
print(cohort.isnull().sum())

#check for duplicate values and then clean
print(cohort.duplicated().sum())

#clean duplicated
cohort=cohort.drop_duplicates()
print(cohort.duplicated().sum())


#describe data after cleaning nan and duplicated vals
print(cohort.describe())

#print the shape of data
print(cohort.shape)

#parse dates in index (definitely need it)

cohort['Date']=pd.to_datetime(cohort['Date'], infer_datetime_format=True)
indexeddf=cohort.set_index(['Date'])
#print(indexeddf)


#parsing to time format and extracting dates with 'created_at'
x=cohort['Date']=pd.to_datetime(cohort['Date'], format='%y-%m-%d')

Day=cohort['Date'].dt.day_name()
Month=cohort['Date'].dt.month
Year=cohort['Date'].dt.year

#subsetting 
cohort['Year']=cohort['Date'].dt.year
cohort['Month']=cohort['Date'].dt.month
cohort['Day']=cohort['Date'].dt.day
#print(cohort)


# Problems_solved distribution

plt.rcParams['figure.figsize'] = (15, 8)
sns.countplot(cohort['Problems_solved'], palette = 'Blues')
plt.title('Distribution of problems solved', fontsize = 20)
plt.show()


#Clusters


x = cohort.iloc[:, [3, 4]].values

# let's check the shape of x
print(x.shape)

from sklearn.cluster import KMeans

"""wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    km.fit(x)
    wcss.append(km.inertia_)
    
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method', fontsize = 20)
plt.xlabel('No. of Clusters')
plt.ylabel('wcss')
plt.show()"""


km = KMeans(n_clusters = 5, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_means = km.fit_predict(x)

plt.scatter(x[y_means == 0, 0], x[y_means == 0, 1], s = 100, c = 'pink', label = 'miser')
plt.scatter(x[y_means == 1, 0], x[y_means == 1, 1], s = 100, c = 'yellow', label = 'general')
plt.scatter(x[y_means == 2, 0], x[y_means == 2, 1], s = 100, c = 'cyan', label = 'target')
plt.scatter(x[y_means == 3, 0], x[y_means == 3, 1], s = 100, c = 'magenta', label = 'spendthrift')
plt.scatter(x[y_means == 4, 0], x[y_means == 4, 1], s = 100, c = 'orange', label = 'careful')
plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:, 1], s = 50, c = 'blue' , label = 'centeroid')

plt.style.use('fivethirtyeight')
plt.title('K Means Clustering', fontsize = 20)
plt.xlabel('ID')
plt.ylabel('Problems_solved')
plt.legend()
plt.grid()
plt.show()


























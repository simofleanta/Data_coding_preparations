import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import stats
 
#open the file
bikes=pd.read_csv('bikes_h.csv')
print(bikes.columns)
df=DataFrame(bikes)

print(df.head(3))

#extract column
cnt=df['cnt']
print(cnt.head(3))


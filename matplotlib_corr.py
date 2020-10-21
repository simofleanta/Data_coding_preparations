
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

bike=df[['cnt','hr','workingday','weekday']].copy()


#heatmap
plt.figure(figsize=(10,5))
sns.heatmap(bike.corr(),cmap='Blues')
plt.show()
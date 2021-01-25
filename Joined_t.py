import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt 


#open file
j=pd.read_csv('joined_t.csv')
print(j.columns)
ba=DataFrame(j.head(21))
print(ba.head(21))

#scatter subplot
f,axes = plt.subplots(1,2, figsize=(15, 10))
A=sns.scatterplot(ba.Salary, ba.KPI, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0]).set_title("Relationship between KPI and income")

B=fig2=sns.boxplot(ba.Location, ba.KPI, palette='viridis',hue_order=[True,False], ax=axes[1]).set_title("KPI per Location")

plt.show()

sns.heatmap(ba.corr(), annot=True, cmap='Blues', linewidth=1,vmin=-1,vmax=1, yticklabels=True,xticklabels=True).set_title("Corelation heatmap")
plt.show()










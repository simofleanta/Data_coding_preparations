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

#open file
finance=pd.read_csv('Margin_Analysis.csv')
print(finance.columns)
df_v=DataFrame(finance.head(120))
print(df_v.head(120))

"""fig, ax=plt.subplots(figsize=(5,4))
sns.set_style('darkgrid')
df_v.groupby('Year')['raised_amount'].count().sort_values().plot(kind='bar')
plt.ylabel('raised_amount')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('raised_amount in years')
plt.show()"""





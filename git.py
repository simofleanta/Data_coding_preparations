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


git=pd.read_csv('GitHub_data.csv')
print(git.columns)
df=DataFrame(git.head(20))
print(df.head(20))


c=df.dtypes
c_missing=df.isnull().sum()
print(c_missing)



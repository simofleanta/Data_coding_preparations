import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import sklearn.preprocessing
from sklearn.metrics import r2_score
import plotly.io as pio
import datetime
import plotly

g=pd.read_csv('enexis_electricity_01012020.csv')
#print(g.columns)
df_nl=DataFrame(g)
print(df_nl.columns)
print(df_nl.head(10))


def normalize_data(df):
    scaler = sklearn.preprocessing.MinMaxScaler()
    df['annual_consume']=scaler.fit_transform(df['annual_consume'].values.reshape(-1,1))
    return df

df_norm = normalize_data(df_nl)

shape=df_norm.shape
#print(shape)
#print(df_norm.head(3))


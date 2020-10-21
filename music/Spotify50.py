import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly
 
#open the file
s=pd.read_csv('Spotify50.csv')
print(s.columns)
df=DataFrame(s)


#no missing_v
m=missing_v=df.isnull().sum()
print(m)
vc=df['Loudness_DB'].value_counts()
print(vc)

#check dtypes
types=df.dtypes
print(types)

#function to fix dtatypes

def fixing_datatypes(df):
    """Fixing the datatypes"""
    df[['Genre']] = df[['Genre']].astype('category')

    Genres_map={1:"Canadian_Pop",2:"Reggaeton_flow",3:"Dance_Pop",4:"Pop",5:"Dfw_rap",6:"Trap_music",7:"Country_rap",8:"Electro_Pop",9:"Reggaeton",10:"Panamanian_Pop",
    11:"Latin",12:"Dfw_rap",13:"Escape_room",14:"Pop house",15:"Australian_Pop",16:"Edm",17:"Atl_hip_hop",18:"big_room",19:"Panamanian_Pop",20:"Brostep"}

    df["Genre"] = df.Genre.map(Genres_map)

    return df
    genre_cat = fixing_datatypes(genre_cat)
    df=fixing_datatypes(df)

    


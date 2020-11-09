import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly


#open the file
cars=pd.read_csv('CarPrice.csv')
print(cars.columns)
df=DataFrame(cars)
print(df.head(3))
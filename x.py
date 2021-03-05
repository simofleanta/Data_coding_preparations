
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


#replace vlookup with python
#I don't have the package but will leave the code on just for future need

# open
#another way of opening files
initial_workbook='dropship.xlsx'
info_workbook='replace_vlookup.xlsx'
#make an output workbok because we'll need info to be outputed in here
output_workbook='output.xlsx'

#pd excel readers
df_initial=pd.read_excel(initial_workbook)
df_info=pd.read_excel(info_workbook)

#print columns
print(df_initial.columns)
print(df_info.columns)

#Since in both docs we have same neme for a column, that is "Code"; we'll rename columns code to IDs
df_initial.rename(columns={'code':'Ids'}, inplace=True)

#merge the 2 columns (like a left join in sql)

df_3=pd.merge(df_initial, df_info[['IDs', 'ID']], on='IDs', how='left')
#print(df_3)

#once doc is printed we'll get some nan values which will need to be droped.
#Also change IDs to Code name

#rename to back to code
df_3.rename(columns={'IDs':'code'}, inplace=True)

#get rif of nen vals
df_3=df_3.replace(np.nan, '', regex=True)
#print(df_3)

#export in excel file and also get rif of index
df_3.to_excel(output_workbook, index=False)
#print df_3 










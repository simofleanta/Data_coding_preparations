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

hr=pd.read_csv('hr.csv')
print(hr.columns)
df=DataFrame(hr.head(113))
print(df.head(113))




# more jobs applied for seem graduate 
sns.violinplot(x=df["Job_seniority"], y=df["interview_call"], palette="Blues")

sns.violinplot(x=df["region"], y=df["interview_call"], palette="Blues")


#aggregation 
operations=['mean','sum','min','max']
a=df.groupby(['Job_seniority','Domain'], as_index=False)[['interview_call']].agg(operations)
#print(a.reset_index())

x=df.groupby(['Domain'])[['interview_call']]
#print(x.count())

y=df.groupby(['interview_call'])
#print(y.count())

#filter interview call 1 
interview_call=df[df.interview_call==1]
No_interview_call=df[df.interview_call==2]
No_answer_interview_call=df[df.interview_call==3]
#print(interview_call)

""" count how many 1=yes interviews by  domain"""
#am having 
yes=interview_call.groupby(['Domain'])
#print(yes.count())

#am not having interview
no=No_interview_call.groupby(['Domain'])
#print(no.count())

#am not having an answer
no_answer=No_answer_interview_call.groupby(['Domain'])
#print(no_answer.count())

""" count how many interviews based on job seniority"""

#am having 
seniority=interview_call.groupby(['Job_seniority'])
print(seniority.count())

#filter seniority with answer 1(it seems that I get nothing on Graduate level wtf....)
#so to filter based on an answer use filtered data on the answer desired
Junior=interview_call[interview_call.Job_seniority=='Junior']
#print(Junior)

#normal jobs are mostly 1 (wonder why?)
Normal=interview_call[interview_call.Job_seniority=='Normal']
#print(Normal)


#image bi 
domain=interview_call[interview_call.Domain=='data intelligence']
print(domain.count())

#image data
domain=interview_call[interview_call.Domain=='data']
print(domain)
domain=interview_call[interview_call.Domain=='data']
print(domain.count())

#imge on region

region_br=interview_call[interview_call.region=='Brussels']
print(region_br)

region_b=interview_call[interview_call.region=='Berlin']
print(region_b)































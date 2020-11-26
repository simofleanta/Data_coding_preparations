import json
import pandas as pd
from pandas import DataFrame 
import numpy as np
import time

with open('datelazi.json', 'r') as file:
    s=json.load(file)

#extract info from the nested json

"""print(s['charts']['dailyStats']['contains'])
print(s['C'])
print(s['currentDayStats']['numberCured'])
print(s['currentDayStats']['numberInfected'])
print(s['currentDayStats']['numberDeceased'])
print(s['currentDayStats']['percentageOfMen'])
print(s['currentDayStats']['percentageOfWomen'])
print(s['currentDayStats']['distributionByAge'])
print(s['C']['countyInfectionsNumbers'])"""

   
with open('stats.json') as file:
    for line in file:
        data=json.loads(line)
    ww=pd.DataFrame(data)
df=pd.read_json("stats.json")
bn=pd.DataFrame(df._get_data_from_filepath())['data']









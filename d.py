import json
import pandas as pd
from pandas import DataFrame
import numpy as np
import time

with open('datelazi.json', 'r') as file:
    s=json.load(file)

print(type(s))



#extract info from the nested json

"""print(s['charts']['dailyStats']['contains'])
print(s['currentDayStats'])
print(s['currentDayStats']['numberCured'])
print(s['currentDayStats']['numberInfected'])
print(s['currentDayStats']['numberDeceased'])
print(s['currentDayStats']['percentageOfMen'])
print(s['currentDayStats']['percentageOfWomen'])
print(s['currentDayStats']['distributionByAge'])
print(s['currentDayStats']['countyInfectionsNumbers'])"""



with open('datelazi.json') as file:
    for line in file:
        data=json.loads(line)
    ww=pd.DataFrame(data)
print(ww)


    







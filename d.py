import json

with open('datelazi.json', 'r') as file:
    s=json.load(file)

#extract info from the nested json

print(s['charts']['dailyStats']['contains'])
print(s['currentDayStats'])
print(s['currentDayStats']['numberCured'])
print(s['currentDayStats']['numberInfected'])
print(s['currentDayStats']['numberDeceased'])
print(s['currentDayStats']['percentageOfMen'])
print(s['currentDayStats']['percentageOfWomen'])
print(s['currentDayStats']['distributionByAge'])
print(s['currentDayStats']['countyInfectionsNumbers'])



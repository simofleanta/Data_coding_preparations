#A function that exxtracts blood type per country
def bloodtype(mdv):
    print(mdv)
    mdv=bo[bo.Country=='Zimbábue']      

bloodtype(mdv=bo[bo.Country=='Zimbábue'])


#----------------------------------------------------------

#Function that counts bloddtype percentages per country. (2 arguments)
# Since there are 2 arguments there is bloodtype percentage per country 
sdv=bo[bo.Country=='Suécia'] 
s=bo['Country']
def bloodcount(counts,country):
    print(counts,country)
    s=bo['Country']
    typecounts=bo['O+'].head(20).value_counts()     

bloodcount(counts=bo['O+'].tail(2).value_counts(),country=s.tail(2)) 
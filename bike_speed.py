#--------------------------------------

#SPEED ON LANES

#if cyclists increase speed to their work by 30% and then by 10% what % of  speed of the original ride would be their total increase?
# we need to find the total % increase
#dearting from the initial ride value increase other 30.then increase by 10% whock gives the final speed increase. calculate final speed as %.


bike_speed=bike_df[['Year','Month','Day','Total_minutes_ride','Number_blocks_to_office','Ride_speed']].copy()
print(bike_speed)

bike_speed['First_Increase']=bike_speed.Ride_speed * 0.3
bike_speed['Increase2']=bike_speed.First_Increase*0.1
bike_speed['All_Speed_Increase']=bike_speed.Increase2+bike_speed.First_Increase
bike_speed['Final_Speed_As_p']=bike_speed.Ride_speed*43/100
print(bike_speed)

#plotting consumption patterns before app 


f,axes = plt.subplots(2,2, figsize=(15,30))
K0=sns.scatterplot(bike_speed.Total_minutes_ride, bike_speed.Ride_speed, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0,0])

k1=sns.stripplot(x='Day', y='Final_Speed_As_p',jitter=0.25, marker='*',alpha=0.6, size=10, linewidth=1, palette="Blues", data=bike_speed, \
    ax=axes[0,1])

k2=sns.boxplot(bike_speed.Day, bike_speed.Final_Speed_As_p, palette='Blues',hue_order=[True,False],ax=axes[1,0])

k3=sns.scatterplot(bike_speed.Number_blocks_to_office, bike_speed.Final_Speed_As_p, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues', ax=axes[1,1])

plt.show()
import random

#rolling a dice

min=1
max=10

roll="Go"

while roll=="Go" or roll=="Roll":
    print("Rolling dice")
    print("Number is...")
    print(random.randint(min,max))
    print(random.randint(min,max))
    
    roll=input("Roll again...")

    





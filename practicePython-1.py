import datetime

today = datetime.date.today() #Getting today's DATE
year = today.year #Getting year portion for Today's DATE

input = int(input("Please enter your age: ")) #Usr Input for AGE, type "int"

hundred = (year - input) + 100 #math to calculate when AGE = 100

print("You will be 100 yrs old in ", hundred) #print output

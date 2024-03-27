input = int(input("Please enter an integer: ")) #Usr input for integer, type "int"
x = list(range(1,input+1)) #setting range of linearly increasing values

output = [] #creating empty list to fill with values later

for i in x: #filling list "output" with divisors of integer with no remainder
    if input % i == 0:
        output.append(i)
    else:
        pass
print(output)



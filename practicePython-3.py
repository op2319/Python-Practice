a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] #pre-defined list
b = [] #empty list to fill

for i in a: #filling list b with all values less than or equal to 5
    if  i <= 5:
        b.append(i)
    else:
        pass
print(b) #print output

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] #pre-defined list 1
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] #pre-defined list 2
c = []


for i in a and b:
    if i in a and b:
        c.append(i)
    else:
        print("No MATCH!")
print(c)

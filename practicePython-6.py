input = input(str("Please enter a word: "))
b = input[::-1]

if b == input:
    print("This is a palindrone!")
else:
    print("This is NOT palindrone!")

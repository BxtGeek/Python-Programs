# Take integer inputs till the user enters 0 and print the sum of all numbers (HINT: while loop)

total = 0
while True:
    x = int(input("Enter the value of x :"))
    if x == 0:
        break
    else:
        total = total + x
print("Sum of the entered numbers:", total)
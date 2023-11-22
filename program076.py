# Take integer inputs till the user enters 0 and print the largest number from all.

largest_number = []
while True:
    x = int(input("Enter the value of x :"))
    if x == 0:
        break
    else:
        largest_number.append(x)
print(largest_number)
if len(largest_number) == 0:
    print("There is no number")
else:
    max_number = max(largest_number)
    print(f"The largest number is {max_number}")
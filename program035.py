#Input a year and find whether it is a leap year or not.

x = int(input("Enter a year: "))
if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")

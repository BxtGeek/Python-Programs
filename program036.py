# Take a number as input and print the multiplication table for it.
x = int(input("Enter the number which you want table of:"))
i = 0
while i <= 10:
    print(f"{x}x{i}=",x*i)
    i += 1
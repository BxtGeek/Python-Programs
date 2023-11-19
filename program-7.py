#float divide operation
x = float(input("Value of X?"))
y = float(input("Value of y?"))

z = x/y
print (f"divide:{z}")

# round decimal point
z = round(x/y,2)
print (f"divide:{z}")

# round decimal point, method#2
z = x/y
print (f"divide:{z:.2f}")
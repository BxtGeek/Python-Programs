"""
interger
in programming we have operator like +,-,*,/,%
we use % to print the reminder of any numner  
"""
x = input("What is the value of x?")
y = input("What is the value of y?") 

# by default python take input as string so we need to convert that into a int
x = int(x)
y = int(y)
z = x+y
print(f"sum={z}")

# method#2
z = int(x)+int(y)
print(f"sum={z}")

# method#3
z = int(x+y)
print(f"sum={z}")

# method#4
print(f"sum={x+y}")
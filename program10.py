"""
understanding operator
>   greater than
>=  greater than or equal to
<   less than
<=  less than or equal to
==  equal to
=   use to assign value
!=  note equal to
"""

# int this program will compare two integer provider by user

x = int(input("What is the value of x:"))
y = int(input("What is the value of y:"))

if x < y:
    print("x is less than y")
if x > y:   
    print("y is greater than x")
if x == y:
    print("x is equal y")
    
"""
if we add elif in the program it will run and give the same output but when the condition satisfy 
it exit from the program, but where as in if it will run and test all the condition
using elif we can improve the perfromance of the program but as our system are so fast it will not 
reflect but when we run big program it will matter alot
"""
"""
x x x x x 
x x x x 
x x x 
x x  
x 
"""
num = 5
for i in range(5):
    for j in range(num-i):
        print("x",end=" ")
    print()
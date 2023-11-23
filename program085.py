"""
x x x x x 
  x x x x 
    x x x 
      x x  
        x 
"""
n = 5
for i in range(n):
    for j in range(n-i):
        print(f" "*i,"x",end=" ")
    print()
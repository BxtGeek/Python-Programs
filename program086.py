"""
        x
      x x
    x x x
  x x x x
x x x x x
"""
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("x",end=" ")
    print()
# Volume Of Cone 

import math
def main():
    x = int(input("Enter the value of radius:"))
    y = int(input("Enter the value of height:"))
    print(f"Volume Of Cone : {cone_volume(x,y):.2f}")

def cone_volume(m,n):
    return math.pi*m*m*(n/3)

main()
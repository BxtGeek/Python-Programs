# Volume Of Cylinder

import math

def main():
    x = int(input("Enter the value of radius:"))
    y = int(input("Enter the value of height:"))
    print(f"Volume Of Cylinder is {volume_cylinder(x,y):.2f}")

def volume_cylinder(m,n):
    return math.pi*m*m*n

main()
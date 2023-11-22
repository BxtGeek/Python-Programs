# Curved Surface Area Of Cylinder

import math

def main():
    x = int(input("Enter the value of radius:"))
    y = int(input("Enter the value of height:"))
    print(f"Curved Surface Area Of Cylinder : {curved_surface_area_cylinder(x,y):.2f}")

def curved_surface_area_cylinder(m,n):
    return 2*math.pi*m*n

main()
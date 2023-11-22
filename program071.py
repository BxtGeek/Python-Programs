# Total Surface Area Of Cube

import math

def main():
    x = int(input("Enter the value of a side :"))
    print(f"Total Surface Area Of Cube : {total_surface_area_of_cube(x)}")

def total_surface_area_of_cube(n):
    return 6*pow(n,2)

main()
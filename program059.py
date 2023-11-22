# Area Of Equilateral Triangle

import math

def main():
    x = int(input("Enter the value of a side:"))
    print(f"Area of Equilateral Triangle is {area_equilateral_triangle(x):.2f}")

def area_equilateral_triangle(m):
    return (math.sqrt(3)*m*m)/4

main()
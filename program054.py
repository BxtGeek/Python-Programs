# Calculate the area and circumference of a circle.

import math

def main():
    x = float(input("Enter the radius of a circle:"))
    x = circumference(x)
    print(f"circumference of circle is : {x:.2f}")

def circumference(n):
    return 2*math.pi*n

main()
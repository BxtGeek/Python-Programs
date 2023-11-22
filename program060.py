# Perimeter Of Circle
import math

def main():
    r = int(input("Enter the value of radius:"))
    print(f"Perimeter of Circle is {perimeter_circle(r):.2f}")

def perimeter_circle(m):
    return 2*math.pi*m

main()
# Volume Of Sphere

import math
def main():
    x = int(input("Enter the value of radius:"))
    print(f"Volume Of Sphere: {volume_sphere(x):.2f}")

def volume_sphere(n):
    return 4*(math.pi*pow(n, 3))/3

main()
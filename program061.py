# Perimeter Of Equilateral Triangle

def main():
    x = int(input("Enter the value of a side :"))
    print(f"Perimeter Of Equilateral Triangle is {perimeter_equilateral_triangle(x)}")

def perimeter_equilateral_triangle(n):
    return 3*n

main()
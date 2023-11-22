# Area Of Isosceles Triangle

def main():
    x = int(input("Enter the value of base :"))
    y = int(input("Enter the value of height :"))
    print(f"Area of Isosceles Triangle is {area_isosceles_triangle(x,y)}")

def area_isosceles_triangle(m,o):
    return (m*o)/2

main()
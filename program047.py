# Calculate the area of a triangle given its base and height.

def main():
    base = int(input("Enter the value of base:"))
    height = int(input("Enter the value of height:"))
    area = int(triangle_area(base,height))
    print("Area of Triangle:",area)

def triangle_area(x,y):
    z = (x*y)/2
    return z

main()
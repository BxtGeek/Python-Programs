#Area Of Rectangle Program

def main():
    x = int(input("Enter the Length of the rectangle:"))
    y = int(input("Enter the Length of the rectangle:"))
    print(f"Area of rectangel is : {rectangle_area(x,y)}")

def rectangle_area(m,n):
    return m*n

main()
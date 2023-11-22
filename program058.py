# Area Of Rhombus

def main():
    x = int(input("Value of First Diagonal:"))
    y = int(input("Value of Second Diagonal:"))
    print(f"Area of Rhombus is {area_rhombus(x,y)}")

def area_rhombus(m,n):
    return (m*n)/2

main()
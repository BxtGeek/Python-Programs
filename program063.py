# Perimeter Of Rectangle

def main():
    x = int(input("Enter the value of side:"))
    y = int(input("Enter the value of base:"))
    print(f"Perimeter Of Parallelogram is {perimeter_rectangle(x,y)}")

def perimeter_rectangle(m,n):
    return 2*(m+n)

main()
# Perimeter Of Parallelogram

def main():
    x = int(input("Enter the value of side:"))
    y = int(input("Enter the value of base:"))
    print(f"Perimeter Of Parallelogram is {perimeter_parallelogram(x,y)}")

def perimeter_parallelogram(m,n):
    return 2*(m+n)

main()
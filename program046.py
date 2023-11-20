#Find the largest among three numbers.

def main():
    x = int(input("Enter the value of x:"))
    y = int(input("Enter the value of y:"))
    z = int(input("Enter the value of z:"))
    find_largest(x,y,z)

def find_largest(m,n,o):
    if m >= n and m >= o:
        print(f"{m} is the largest number")
    elif n >= m and n >= o:
        print(f"{n} is the largest number")
    else:
        print(f"{o} is the largest number")

main()
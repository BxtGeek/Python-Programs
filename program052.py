#Find the square root of a number.

def main():
    x = int(input("Enter a number:"))
    y = square(x)
    print(f"The square root of {x} is {y}")

def square(n):
    n = n*n
    return n

main()
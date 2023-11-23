# Factorial Program

def main():
    x = int(input("Enter the value of x :"))
    print(f"Factorial of {x} is {factorial(x)}")

def factorial(n):
    count = 1
    for i in range(1,n+1):
        count = count*i
    return count

main()
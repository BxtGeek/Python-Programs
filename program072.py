# Fibonacci Series Programs

def main():
    x = int(input("Enter the number of terms for Fibonacci series: "))
    fibonacci(x)

def fibonacci(n):
    a, b = 0, 1
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci series up to", n, "term:")
        print(a)
    else:
        print("Fibonacci series:")
        print(a, b, end=" ")
        for i in range(2, n):
            c = a + b
            print(c, end=" ")
            a, b = b, c

main()
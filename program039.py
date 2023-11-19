#To calculate Fibonacci Series up to n numbers.

def main():
    x = int(input("Enter the value of X:"))
    fibonacci(x)

def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    print(f"Fibonacci sequence of {n} numbers: {fib_sequence}")

main()
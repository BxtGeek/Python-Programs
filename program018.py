# imporving program17 with funtion

def main():
    x = int(input("Value of x:"))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    # return True if n % 2 == 0 else False
    # return if n % 2 == 0
main()
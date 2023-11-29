# print square of any number

def main():
    x = int(input("Enter the number :"))
    print(f"sqaure of {x} is", square(x))

def square(n):
    return n*n

if __name__ == "__main__":
    main()
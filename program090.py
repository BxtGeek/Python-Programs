def main():
    while True:
        try:
            x = int(input("Enter a value of x :"))
        except ValueError:
            print("x is not a integer")
        else:
            break
    
    print_number(x)
def print_number(n):
    print(f"X Number is :{n}")
main()
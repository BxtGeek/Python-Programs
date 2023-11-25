# further refirment of the coe program#90

def main():
    while True:
        try:
            x = int(input("Enter a value of x :"))
            break
        except ValueError:
            print("x is not a integer")
    print_number(x)

def print_number(n):
    print(f"X Number is :{n}")

main()
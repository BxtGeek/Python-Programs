# further refirment of the coe program#91

def main():
    x = print_number()
    print(f"x is {x}")

def print_number():
    while True:
        try:
            return int(input("Enter a integer :"))
        except ValueError:
            # we can also use pass insted of printing it will again pass to the print statement 
            pass
            #print("x is not a integer")

main()
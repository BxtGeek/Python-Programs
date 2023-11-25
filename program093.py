# further refirment of the coe program#92

def main():
    x = print_number("Enter a integer :")
    print(f"x is {x}")

def print_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # we can also use pass insted of printing it will again pass to the print statement 
            pass
            #print("x is not a integer")

main()
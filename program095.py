# program to flip a coin second method
from random import choice

def main():
    choice = user_input()
    result = generate()
    determine_winner(choice,result)

def user_input():
    while True:
        try:
            choice = int(input("select 1 for heads and 2 for tails :"))
            if choice in (1,2):
                return choice
            else:
                print("Please enter either 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
def generate():
    return choice(["heads","tails"])

def determine_winner(choice,result):
    if (choice == 1 and result == "heads") or (choice == 2 and result == "tails"):
        print("You Win!")
    else:
        print("You lose!")

main()
# stone paper scissor game
import random

def main():
    x = int(input("Select 1 for Stone, Select 2 for paper and Select 3 for scissor:"))
    game(x)

def game(n):
    if n in [1,2,3]:
        options = {1: "Stone", 2: "Paper", 3: "Scissor"}
        y = random.randint(1, 3)
        
        print(f"Your choice {n}")
        print(f"computer choice {y}")

        if n == y:
            print("Game Tie!")
        
        elif (n == 1 and y == 3) or (n == 2 and y == 3) or (n ==3 and y == 1):
            print("You Win!")

        else:
            print("You Loose!")

    else:
        print("Please Enter correct Value, Select 1 for Stone, Select 2 for paper and Select 3 for scissor")


main()
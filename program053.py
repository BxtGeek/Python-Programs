# Generate a random number between a given range.
import random

def main():
    x = int(input("Enter the Straing Number:"))
    y = int(input("Enter the Ending Number:"))
    random_number(x,y)

def random_number(m,n):
    o = random.randrange(m,n)
    print(f"Random number between {m} and {n} is {o}")

main()
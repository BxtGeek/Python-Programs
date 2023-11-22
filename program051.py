#Check if a string is a pangram or not.
    
def main():
    x = list(input("Enter a String: "))  # Convert input string to a list of characters
    y = pangram(x)

def pangram(n):
    count = 0
    alphabet = set("abcdefghijklmnopqrstuvwxyz")  # Use a set for faster lookup
    present_letters = set()
    for i in n:
        if i.isalpha():
            present_letters.add(i.lower())  # Store only lowercase letters to check for uniqueness
    if alphabet.issubset(present_letters):  # Check if the alphabet set is a subset of present_letters
        print("The entered string is a pangram.")
    else:
        print("The entered string is not a pangram.")

main()

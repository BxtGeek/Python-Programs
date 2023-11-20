# Check if a given word is a palindrome.

def main():
    x = input("Enter the value of x:")
    palindrome(x)

def palindrome(x):
    y = x[::-1]
    if x == y:
        print(f"{x} is a palindrome of {y}")
    else:
        print(f"{x} is a not palindrome of {y}")

main()
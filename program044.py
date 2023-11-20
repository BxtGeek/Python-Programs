#Reverse a String

def main():
    x = input("Enter a word:")
    y = reverse(x)
    print(f"Reverse String of {x} is {y}")

def reverse(n):
    return n[::-1]    # use slicing

main()
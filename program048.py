# Count the number of vowels in a string.

def main():
    x = input("Enter a string:")
    count = count_vowels(x)
    print(f"vowels in string{x} are {count}")

def count_vowels(a):
    count = 0
    vowels = "aeiouAEIOU"
    for i in a:
        if i in vowels: 
            count = count + 1
    return count

main()
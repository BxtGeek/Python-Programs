# Input a number and print all the factors of that number (use loops).

def main():
    x = int(input("Enter a integer :"))
    print_factors(x)

def print_factors(n):
    all_factor = []
    for i in range(1,n+1):
        if n % i == 0:
            all_factor.append(i)
    print(all_factor)
    
main()
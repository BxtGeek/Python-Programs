#Check if a number is prime or not.
def main():
    num = int(input("Enter a number:"))
    prime(num)

def prime(n):
    if n <= 0:
        print("Only positive number are prime")
    else:
        mod = 0
        for i in range(1,n+1):
            if n % i == 0:
                mod += 1
        if mod == 2:
            print(n,"is a prime number")
        else:
            print(n,"is not a prime numner")

main()

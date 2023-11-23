# A person is eligible to vote if his/her age is greater than or equal to 18. Define a method to find out if he/she is eligible to vote.

def main():
    x = int(input("Enter the age:"))
    eligible_age(x)

def eligible_age(n):
    if n >= 18:
        print("person is eligible for vote")
    else:
        print("person is not eligible for vote")

main()
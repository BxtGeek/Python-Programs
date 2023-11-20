#Create a simple interest calculator.

def main():
    p = int(input("Enter the value of principal:"))
    r = int(input("Enter the value of Range:"))
    t = int(input("Enter the value of Time:"))
    result = simple_intrest(p,r,t)
    print("Simple Interest:", result)

def simple_intrest(x,y,z):
    si = (x*y*z)/100
    return si

main()
def main():
    x = int(input("Whats is the value of x:"))
    print ("x squared is",square(x))
    
def square(n):
    return n*n
    # we can also use the below syntax
    # return n**2
    # return pow(n,2)

main()
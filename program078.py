# Define two methods to print the maximum and the minimum number respectively among three numbers entered by the user.

def main():
    x = int(input("Enter the value of x :"))
    y = int(input("Enter the value of y :"))
    z = int(input("Enter the value of z :"))
    print(f"The minimum number amoung {x,y,z} is {min_number(x,y,z)} and the The maximum number is {max_number(x,y,z)}")

def min_number(m,n,o):
    if m <= n and m <= o:
        return m
    elif n <= m and n <= o:
        return n
    else:
        return o

def max_number(m,n,o):
    if m >= n and m >= o:
        return m
    elif n >= m and n >= o:
        return n
    else:
        return o

main()
# Subtract the Product and Sum of Digits of an Integer

def main():
    x = int(input("Enter the value of x:"))
    y = product_of_digit(x) - sum_of_digit(x)
    print("Difference is:", y)

def sum_of_digit(n):
    digits = []
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n //= 10
    digits_sum = sum(digits)
    return digits_sum

def product_of_digit(n):
    digits = []
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n //= 10
    product_digit = 1
    for i in digits:
        product_digit *= i
    return product_digit

main()

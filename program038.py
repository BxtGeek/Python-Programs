#Input currency in rupees and output in USD.

def main():
    x = float(input("Enter the value in INR:"))
    convert_usd(x)

def convert_usd(n):
    usd_value = 83.29*n
    print(f"{n} in usd will be {usd_value:.2f}") 

main()
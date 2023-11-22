# Volume Of Pyramid

def main():
    x = int(input("Enter the value of length:"))
    y = int(input("Enter the value of width:"))
    z = int(input("Enter the value of height:"))
    print(f"Volume Of Pyramid : {volume_pyramid(x,y,z):.2f}")

def volume_pyramid(m,n,o):
    return (m*n*o)/3
main()
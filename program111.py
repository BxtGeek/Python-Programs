# Given an integer array arr of size n, you need to sum the elements of arr.

def main():
    x = int(input("How many element you want in array :"))
    arr = arr_input(x)
    count = array_sum(arr)
    print("The sum of array is:",count)
def arr_input(n):
    arr = []
    for i in range(n):
        arr.append(int(input(f"Enter the value in {i} placed:")))
    return arr

def array_sum(arr):
    count = 0
    for i in range(len(arr)):
        count = count + arr[i]
    return count  
  
main()
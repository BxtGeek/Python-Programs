# You are given an array A of size N. You need to print elements of A in alternate order (starting from index 0).
def main():
    x = int(input("Enter the number of elements in the array: "))
    arr = input_arr(x)
    print_alt_arr(arr)
    
def input_arr(n):
    arr = []
    for i in range(n):
        arr.append(int(input(f"Element at index {i}: ")))
    return arr

def print_alt_arr(arr):
    for i in range(len(arr)):
        if i % 2 == 0:  # Check if the index is even
            print(arr[i], end=" ")
    print() 
main()

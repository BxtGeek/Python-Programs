"""
Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).
"""

def main():
    x = int(input("How many element you need in array :"))
    arr = arr_input(x)
    arr_index(arr)
    
def arr_input(n):
    arr = []
    for i in range(n):
        arr.append(int(input(f"Enter the value in {i} place :")))
    return arr
    
def arr_index(arr):
    for i in range(len(arr)):
        if arr[i] == i + 1:
            print(f"Element {arr[i]} at index {i + 1} matches the condition.")
        else:
            print("No matching condition found.")
            
main()
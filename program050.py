#Calculate the average of numbers in a list.

def main():
    array = array_input()
    avg = array_average(array)
    print(f"The average of the elements in the array is: {avg}")

def array_input():
    array = []
    n = int(input("Enter how many element you want in your array:"))
    for i in range(n):
        element = int(input(f"Enter the element in position {i+1}: "))
        array.append(element)
    return array

def array_average(arr):
    if not arr:
        return 0
    total = 0
    for num in arr:
        total += num
    return total/len(arr)

main()
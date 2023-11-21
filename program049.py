#print array in python
array = []
n = int(input("Enter number of elements: "))  # Input the number of elements
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)
print(array)

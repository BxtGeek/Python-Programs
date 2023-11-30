# optimizing the program125.py

with open ("file/name.csv") as file:
    for line in file:
        name,age = line.rstrip().split(",")
        print(f"{name} age is {age}")
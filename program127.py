# optimizing the program126.py

students = []
with open ("file/name.csv") as file:
    for line in file:
        name,age = line.rstrip().split(",")
        students.append(f"{name} age is {age}")

for i in sorted(students):
    print(i)
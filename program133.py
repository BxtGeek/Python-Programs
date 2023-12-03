# optimizing the program132.py
# will use the lamda function

import csv

students = []

with open("file/name.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "age": row["age"]})

for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} age is {student['age']}")

# optimizing the program130.py
# will use the lamda function
import csv

students = []

with open("file/name.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name":row[0],"age":row[1]})
    """
        # Alternate Approch
        for name,age in reader:
        students.append({"name":name,"age":age})
    """

for student in sorted(students, key=lambda student: student["name"], reverse = True):
    print(f"{student['name']} age is {student['age']}")
# optimizing the program129.py
# will use the lamda function

students = []
with open("file/name.csv") as file:
    for line in file:
        name,age = line.rstrip().split(",")
        student = {"name":name,"age":age}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"], reverse = True):
    print(f"{student['name']} age is {student['age']}")
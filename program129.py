# optimizing the program128.py

students = []
with open("file/name.csv") as file:
    for line in file:
        name,age = line.rstrip().split(",")
        student = {"name":name,"age":age}
        students.append(student)
        
def get_name(student):
    return student["name"]

def get_age(student):
    return student["age"]

for student in sorted(students, key=get_name, reverse = True):
    print(f"{student['name']} age is {student['age']}")
    
print("****************")

for student in sorted(students, key=get_age, reverse = True):
    print(f"{student['name']} age is {student['age']}")
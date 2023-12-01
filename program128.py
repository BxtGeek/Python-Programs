# optimizing the program127.py
# will use dictionary here 

students = []
with open("file/name.csv") as file:
    for line in file:
        name,age = line.rstrip().split(",")
        student = {} # dictornary
        # loading value from file to dictonary
        student["name"] = name
        student["age"] = age
        # insted of using the above approch we can make code more consise using the below line
        # student = {"name":name,"age":age}
        students.append(student)
        
for student in students:
    print(f"{student['name']} age is {student['age']}")
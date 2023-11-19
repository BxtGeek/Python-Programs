student = ["Manoj","Shantanu","Arun"]

# method#1
print("Method#1")  
for i in range(3):
    print(f"Student:{student[i]}")

# method#2  
print("Method#2") 
for i in student:
    print(f"Student:{i}")

# method#3
print("Method#3")  
print(student[0])
print(student[1])
print(student[2])

# method#4
print("Method#4")
for i in range(len(student)):
    print(f"Student:{student[i]}")

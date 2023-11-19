"""
imporving program29 with multiple entry
in this example we added there house name and the pet the own
"""
students = [
    {"Name":"Manoj","House":"Blue","Pet":"Cat"},
    {"Name":"Parul","House":"Blue","Pet":"Dog"},
    {"Name":"Shantanu","House":"Yellow","Pet":"Rabbit"},
    {"Name":"Arun","House":"Yellow","Pet":"Snake"},
    {"Name":"Naveen","House":"Green","Pet":"Grog"},
    {"Name":"Sandesh","House":"Green","Pet":"Rakoon"},
    {"Name":"Furkan","House":"Red","Pet":None},
]

for student in students:
    print(student["Name"],student["House"],student["Pet"],sep=":")
"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
"""
if __name__ == "__main__":
    students = []
    number_student = int(input())
    for i in range(number_student):
        name = input("Enter student's name: ")
        score = float(input("Enter student's score: "))
        students.append([name, score])
    print(students)
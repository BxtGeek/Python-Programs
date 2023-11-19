"""
create a simple python program to calculate the grade of a student
"""

score = int(input("Enter the Score:"))
if score >= 90  and score <= 100:
    print("GRADE:A")
elif score >= 80  and score < 90:
    print("GRADE:B")
elif score >= 60  and score < 80:
    print("GRADE:C")
elif score >= 40  and score < 60:
    print("GRADE:D")
else:   
    print("FAIL")
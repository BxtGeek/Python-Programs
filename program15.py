"""
improving program#14
"""

score = int(input("Enter the Score:"))
if  90 <= score <= 100:
    print("GRADE:A")
elif 80 <=  score < 90:
    print("GRADE:B")
elif 60 <= score < 80:
    print("GRADE:C")
elif 40 <= score < 60:
    print("GRADE:D")
else:   
    print("FAIL")
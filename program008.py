"""
improving program#15
"""

score = int(input("Enter the Score:"))
if  score >= 90:
    print("GRADE:A")
elif score >= 80:
    print("GRADE:B")
elif score >= 60:
    print("GRADE:C")
elif score >= 40:
    print("GRADE:D")
else:   
    print("FAIL")
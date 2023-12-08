"""
Regular Expression - regexes
Will write a code to validate an email
"""
email = input("Enter the Email?").strip()
if "@" in email and "." in email:
    print("Valid")
else:
    print("invalid")
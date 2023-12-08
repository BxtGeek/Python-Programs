# Improving the code program139
email = input("Enter the Email?").strip()
username,domain = email.split("@")

if username and "." in domain:
    print("valid")
else:
    print("invalid")
# Improving the code program140
# we can use this "\." to specify anything after that as a comman statement 
# r in 6 line refer as a raw string
import re
email = input("Enter the Email?").strip()

print("Method#1 - This will take space and line")
if re.search(r".+@.+\.edu",email):
    print("valid")
else:
    print("invalid")

print("Method#2 - This will not take space and line")
if re.search(r"^.+@.+\.edu",email):
    print("valid")
else:
    print("invalid")
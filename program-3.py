# Optimizing the program#2

name = input("What is your Name:").strip().title()
print(f"Hello,{name}")

# strip function will not remove the space between the 2 words 
# we can combine as many as function in a same line

# split user name into first name and last name
first,last = name.split(" ")
print(f"Hello,{first}")
print(f"Hello,{last}")
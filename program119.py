"""
File I/O - using this we can store the data in the persistance storage rather than memory
list - We are able to store multiple value 
"""
names = []
for _ in range(3):
    names.append(input("What's your name?"))
    
for name in sorted(names):
    print(f"hello, {name}")
# optimizing the program123, we want that every time it load the file it will make the name in order

names = []

with open("file/name#1.txt") as file:
    for line in file:
        names.append(line.rstrip())

# print in ascending order
for name in sorted(names):
    print(f"Hello,{name}")

# print in descending order
for name in sorted(names,reverse = True):
    print(f"Hello,{name}")
# optimizing the program119 using file I/O
name = input("What's your name :")
# "w" will recreate the wile everytime if we use "a" it will append in the existing file
file = open("file/name.txt","a")
file.write(f"{name}\n")
file.close()
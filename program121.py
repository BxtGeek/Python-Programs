# optimizing the program121 , we are using with here. Using with we need to not close the file manually

name = input("Enter the name:")
with open("file/name#1.txt","a") as file:
    file.write(f"{name}\n")
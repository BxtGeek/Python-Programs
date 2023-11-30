# read an exisiting file
# using rstrip we can remove the extra conetnt from the line 

with open("file/name#1.txt","r") as file:
    lines = file.readlines()
    
for line in lines:
    print("Hello,",line.rstrip())
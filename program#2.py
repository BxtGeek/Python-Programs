#get input value in python 
name = input("Enter your Name:")

#print normally, while adding , it will automatically added the space
print ("Hello",name)

#print normally, while adding + operator it will not add the space
print ("Hello"+ name)

#using the sep that mean sepration we are overwritting sepration, like what exactly it will use
print ("Hello",name,sep="???")

#explicitly sets the end parameter to new line
print("Hello", end="\n")
print(name)

#explicitly sets the end parameter to add space insated of new line
print("Hello", end=" ")
print(name)

# if we want to add the quotes symbol " in the output then we can use \ to make system realise that they are not the closing statement
print("Hello, \"",name, "\"")

# new method to print name
# we added the f to make python release this is a special string not a normal one 
print(f"Hello,{name}")

# new method to print name without f
# because in this case it is not considiring as a special string 
print("Hello,{name}")

# we can use a string function name strip to remove all the extra space in the string 
# let suppose we input the user name and we added lots of space so it will automatically remove that
# First let format the string, it remove the whitespace 
name = name.strip()

#now let print this 
print(f"Hello,{name}")
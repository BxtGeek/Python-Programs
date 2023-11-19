"""
Now let's talk about the match statement. In python we dont have the switch statement 
We can use the match over here. Like othe program we can the synatx of match will be similar 
there is no chnages but let see with an example
"""

"""
let supose there are 7 friends Manoj, Shantanu, Arun, Furkan, Naveen, Shandesh and Parul. There
houses as follow:
Manoj and Parul => Blue House
Shantanu and Arun => Yellow House
Naveen and Sandesh=> Green House
Furkan => Red House

We need to write a program, Like when a name is enter it will return the house name of that 
student. Let see how we can create that.
"""

name = input("Enter the name:")

match name:
    case "Manoj" | "Parul":
        print("Blue House")
    case "Shantanu" | "Arun":
        print("Yellow House")
    case "Naveen" | "Sandesh":
        print("Green House")
    case "Furkan":
        print("Red House")
    case _:                                 # this is for the default value anything is not the part of any house will go this group
        print("Not a part of any house")
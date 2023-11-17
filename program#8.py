"""
create function in python
will create a simple hello function to print user input
we assign a default value to a vartible in this case x
In this case when we pass the veriable name in hello(name) it print the user name 
but when we did not define the name it took the default value and print that
Also we need to make sure that we need to always had funcation in the start of the program
we can also do on this we can put the statement in main so when ever inepreter 
run it will start with the main funtion
"""

def main():
    name = input("What is your name?")
    hello(name)
    hello()
    
def hello(x="World!"):
    print("Hello",x)
    
main()
# imporvement of program 99

"""
using sys.exit, It will exit the program then and there if condition matches 
"""
import sys

if len(sys.argv) < 2 :
    sys.exit("Too few argument")
        
elif len(sys.argv) > 2 :
    sys.exit("Too many argument")
    
print("Hello, my name is",sys.argv[1])
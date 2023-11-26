# multiple command line argument 

import sys

try:
    print("Hello, my name is", sys.argv[1], "and my age is", sys.argv[2])
except IndexError:
    print("Please enter the name")
# command line argument example
"""
The list of command line arguments passed to a Python script. argv[0] is the script name (it is operating system dependent whether this is a full pathname or not). If the command was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'. If no script name was passed to the Python interpreter, argv[0] is the empty string.

To loop over the standard input, or the list of files given on the command line, see the fileinput module.
"""
import sys

try:
    print("Hello, my name is",sys.argv[1])
except IndexError:
    print("Please enter the name")
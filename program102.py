# improving code program101
# will use slice to avoide the program name
# if add -1 in the slice it will avoide the number form the last

import sys

if len(sys.argv) < 2:
    sys.exit("too few argument")

for arg in sys.argv[1:]:
    print("Hello, My name is",arg)

for arg in sys.argv[1:-1]:
    print("Hello, My name is",arg)
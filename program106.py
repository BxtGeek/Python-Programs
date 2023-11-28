# importing another program in program

import sys
from program105 import print_first_name

if len(sys.argv) == 2:
    print_first_name(sys.argv[1])
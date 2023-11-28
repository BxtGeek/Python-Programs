# pip - it is the package manager in the python
# if we required any additional package in our pogram we can use the pip
# This is the official website for the https://pypi.org/ packages in python that we can use 

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello," + sys.argv[1])
    cowsay.trex("Hello," + sys.argv[1])
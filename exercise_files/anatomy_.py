#!/usr/bin/python

# Example Python script

# importing from the system files

import sys

# creating variable argc (length of sys.argc)
# argv is part of the sys module
# an argument vector a.k.a the list of parameters or inputs to the program

# argc is our variable, argv built into sys
argument_count = len(sys.argv)

# opening an if else statement when greater than one print x if not print y

# 'if' is called a conditional expression
if argument_count > 1:
    print('Too many args')
else:
    # where is a variable whose value is a string 'world'
    where = 'world'
    print("Hello", where)

# if successful print goodbye from + sys.argv

print('Goodbye from ' + sys.argv[0])
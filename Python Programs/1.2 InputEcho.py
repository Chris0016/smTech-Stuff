# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 1.2                      #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal: Teach the student how to read user input, store it, and work with it within a program.

Remarks:

1. Many students struggle conceptually with what's going on when reading input. While a verbal explanation may suffice for some students, a simple pictoral explanation showing how the users input gets read in and stored in a variable may greatly benefit some students.

2. (Python Only) Consider beginning by using input with no arguments (i.e. no prompt string) and have the student print the question beforehand. Many students develop a misconception of how input works, and sometimes attempt to pass the variable they want to read as a parameter.

"""

text = input("Enter a word.")
print(text)

#A simple greeter, for now use + to introduce the idea.
#Later on can teach how to use , to separate parameters
#to print.

username = input("Please enter your username")
print("Hello " + username)

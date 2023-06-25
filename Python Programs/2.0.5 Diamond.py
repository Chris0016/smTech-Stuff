# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 2.0.5                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal: Reinforce and develop mastery using nested for loops.

Remarks:

1. 


"""

x = int(input("Please enter the size of the Diamond. "))

for i in range(x):
  for j in range(x - i - 1):
    print(" ", end = "")
  for j in range(i+1):
    print("* ", end = "")
  print()

for i in range(x):
  for j in range(i+1):
    print(" ", end = "")
  for j in range(x - i -1):
    print("* ", end = "")
  print()

# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 2.0.6                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes:

Goal: Demonstrate mastery of nested for loops. Have students think about
the boundaries of the loop. (i.e. values of i at the start and end of a loop)

Remarks:
1. Let a student try and implement the hollow diamond on their own
before leading them to the answer. 
2. Lead students to the right answer instead of outright telling it to them. 
i.e. "Our code from before is great, but now we only want a star to print IF
it is first or last in the row"
3. Have the student tell you the value of "j," the second index variable, at
the end of each loop. Why is it important to know that? (arrays/lists)
"""

x = int(input("Please enter the size of the Diamond. "))

for i in range(x):
  for j in range(x - i - 1):
    print(" ", end = "")
  for j in range(i+1):
    if (j == 0 or j == i):
      print("* ", end = "")
    else:
      print("  ", end = "")
  print()

for i in range(x):
  for j in range(i + 1):
    print(" ", end = "")
  for j in range(x - i - 1):
    if (j == 0 or j == x - i - 2):
      print("* ", end = "")
    else:
      print("  ", end = "")
  print()

"""
Challenge: Have a user enter in their name, print a hollow diamond around the users name.
"""

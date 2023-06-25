# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 2.0.1                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal: Reinforce for loops.

Remarks:

1. 


"""

#Variation 1 (1-100 all)

for i in range(1, 101):
  print(i)

#Variation 2 (2-100 evens)

for i in range(2, 101, 2):
  print(i)

#Variation 3 (50-1000 by threes)

for i in range(50, 1001, 3):
  print(i)

#Variation 4 (Challenge 1-100 with no multiples of 6)

for i in range(1, 101):
  if not i % 6 == 0:
    print(i)

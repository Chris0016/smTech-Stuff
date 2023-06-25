# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 1.4.4                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal: Introduce the mechanism of a for loop. Introduce additional conditional operators. Show the student how a lot of work can be done with a small amount of code.

Remarks:

1. 


"""

#Variation 1 (1-100 all)

i = 1

while i < 101:
  print(i)
  i = i + 1

#Variation 2 (2-100 evens)

i = 2

while i < 101:
  print(i)
  i = i + 2

#Variation 3 (50-1000 by threes)

i = 50

while i < 10001:
  print(i)
  i = i + 3

#Variation 4 (Challenge 1-100 with no multiples of 6)

i = 1

while i < 101:
  if not i % 6 == 0:
    print(i)
  i = i + 1

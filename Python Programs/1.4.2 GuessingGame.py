# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 1.4.2                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal: Have the student think through how to solve a problem with while loops. Introduce the syntax for finding a random number.

Remarks:

1. 


"""

from random import randint

x = randint(1, 100)

guess = -1
tries = 0

while not guess == x:

  guess = int(input("Please enter a number between 1-100. "))
  tries += 1

  if guess > x:
    print("Too high! ", end = "")

  if guess < x:
    print("Too low! ", end = "")

  if tries == 7 and not guess == x:
    print("You're out of tries, you lose.")
    break
  elif not guess == x:
    print("Try again.")

if guess == x:
  print("You won!")

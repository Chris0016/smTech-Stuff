# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 1.4.3                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal: Further practice with if, while, and random numbers.

Remarks:

1. 


"""

from random import randint

repeat = True

while repeat == True:
  
  #Let rock => 0, scissors => 1, paper => 2
  computer = randint(0, 2)
  
  player = input("Enter [R]ock, [P]aper, or [S]cissors! ")

  if computer == 0:
    
    if player == "R":
      print("It's a tie! Go again.")

    elif player == "P":
      print("You win!")
      repeat = False

    else:
      print("You lost! Go again.")

  if computer == 1:

    if player == "S":
      print("It's a tie! Go again.")
    
    elif player == "R":
      print("You win!")
      repeat = False

    else:
      print("You lost! Go again.")

  if computer == 2:
  
    if player == "P":
      print("It's a tie! Go again.")
    
    elif player == "S":
      print("You win!")
      repeat = False

    else:
      print("You lost! Go again.")

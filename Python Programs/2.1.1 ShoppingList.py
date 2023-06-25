# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 2.1.1                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal: Reinforce the concept

Remarks:

1. 


"""

cart = []

while True:
  
  print(cart)

  ans = input("Would you like to [a]dd or [r]emove to your cart or [e]xit? ")

  if ans == "a":

    ans = input("What would you like to add? ")
    cart.append(ans)

  elif ans == "r":

    ans = input("What would you like to remove? ")

    if ans in cart:
      cart.remove(ans)
    else:
      print("That item is not in your cart!")

  elif ans == "e":
    print(cart)
    break

  else:
    print("Invalid menu option.")

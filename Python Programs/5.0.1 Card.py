# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 5.0.1                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED


class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

  def toString(self):
    result = ""
    if (self.value == 1):
      result += "ace"
    elif (self.value == 11):
      result += "jack"
    elif (self.value == 12):
      result += "queen"
    elif (self.value == 13):
      result += "king"
    else:
      result += str(self.value)

    result += " of " + self.suit + "s"
    return result

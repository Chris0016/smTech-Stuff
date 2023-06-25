# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 5.0.2                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

from Card import Card
from random import randint

class Deck:
  def __init__(self):
    self.deck = []

    for i in range(1, 14):
      for j in range(0, 4):
        if (j == 0):
          self.deck.append(Card("heart", i))
        elif (j == 1):
          self.deck.append(Card("spade", i))
        elif (j == 2):
          self.deck.append(Card("diamond", i))
        else:
          self.deck.append(Card("club", i))

  #For every element in the array, swap it with another
  #element in the array
  def shuffle(self):
    for i in range(len(self.deck)):
      x = randint(i, len(self.deck) - 1)
      temp = self.deck[i]
      self.deck[i] = self.deck[x]
      self.deck[x] = temp

  def draw(self):
    return self.deck.pop()

  def getLength(self):
    return len(self.deck)

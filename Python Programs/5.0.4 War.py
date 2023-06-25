# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 5.0.4                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

from Deck import Deck

deck = Deck()
deck.shuffle()

playerCard = None
player2Card = None

player1 = input("Player 1, enter your name. ")
player2 = input("Player 2, enter your name. ")

score = 0
score2 = 0

while (deck.getLength() > 0):
  player1Card = deck.draw()
  player2Card = deck.draw()
  
  print(player1 + ":", player1Card.toString())
  print(player2 + ":", player2Card.toString())
  
  if (player1Card.value > player2Card.value):
    print(player1, "wins the round.")
    score += 1
  elif (player1Card.value == player2Card.value):
    print("Tie round.")
  else:
    print(player2, "wins the round")
    score2 += 1

  input("Press enter to start the next round. ")

if (score > score2):
  print(player1, "wins with a score of", score)
elif (score == score2):
  print("Tied game!")
else:
  print(player2, "wins with a score of", score2)

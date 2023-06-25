# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #                                
#                                 #
# Module 3.0.1                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

def printBoard(board):

  print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] )
  print(" --------- ")
  print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] )
  print(" --------- ")
  print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] )

def checkWinner(board, letter):

  if board[0][0] == letter and board[0][1] == letter and board[0][2] == letter:
    return True
  
  if board[1][0] == letter and board[1][1] == letter and board[1][2] == letter:
    return True

  if board[2][0] == letter and board[2][1] == letter and board[2][2] == letter:
    return True

  if board[0][0] == letter and board[1][0] == letter and board[2][0] == letter:
    return True

  if board[0][1] == letter and board[1][1] == letter and board[2][1] == letter:
    return True
  
  if board[0][2] == letter and board[1][2] == letter and board[2][2] == letter:
    return True

  if board[0][0] == letter and board[1][1] == letter and board[2][2] == letter:
    return True

  if board[2][0] == letter and board[1][1] == letter and board[0][2] == letter:
    return True

def changeTurn(letter):

  if letter == "x":
    letter = "o"
  else:
    letter = "x"

  return letter

board = []

for i in range(3):
  temp = []
  for j in range(3):
    temp.append(" ")
  board.append(temp)

count = 0
letter = "x"

while count < 9 and count >= 0:
  
  printBoard(board)
  
  x = int(input("Please enter the x-coordinate of your piece. "))
  y = int(input("Please enter the y-coordinate of your piece. "))
  
  board[y][x] = letter
  
  count += 1
  
  if checkWinner(board, letter) == True:
    print(letter, "wins!")
    count = -1
  
  letter = changeTurn(letter)

if count == 9:
  print("Tie game!")

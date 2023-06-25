# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #                                 
#                                 #
# Module 3.0.2                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

def printBoard(board):

  for i in range(7):
    for j in range(7):
      print(board[i][j], end = "")
    print()

def checkWin(board, turn):

  for i in range(7):
    for j in range(4):
      if board[i][j] == turn and board[i][j+1] == turn and board[i][j+2] == turn and board[i][j+3] == turn:
        return True

  for i in range(7):
    for j in range(4):
      if board[j][i] == turn and board[j+1][i] == turn and board[j+2][i] == turn and board[j+3][i] == turn:
        return True

  for i in range(4):
    for j in range(4):
      if board[i][j] == turn and board[i+1][j+1] == turn and board[i+2][j+2] == turn and board[i+3][j+3] == turn:
        return True
  for i in range(3,7):
    for j in range(4):
      if board[i][j] == turn and board[i-1][j+1] == turn and board[i-2][j+2] == turn and board[i-3][j+3] == turn:
        return True

def swapTurn(turn):
  
  if turn == "[x]":
    turn = "[o]"
  else:
    turn = "[x]"

  return turn

def getHeight(heights, x):
  
  y = heights[x]
  heights[x] -= 1

  return y

board = []

for i in range(7):
  row = []
  
  for j in range(7):
    row.append("[ ]")
  
  board.append(row)


count = 0
turn = "[x]"
heights = [6,6,6,6,6,6,6]

while count < 49 and count >= 0:
  
  printBoard(board)
  
  count += 1
  
  x = int(input("Please enter the column you'd like to place your piece [1-7]. "))
  x = x - 1
  y = getHeight(heights, x)
  
  board[y][x] = turn

  if checkWin(board, turn) == True:
    print(turn, "wins!")
    count = -1

  turn = swapTurn(turn)

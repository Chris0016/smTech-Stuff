# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 1.3.1                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal: Practice using and further develop an understanding of if/else statements. Introduce the syntax for incrementing/decrementing a variable.

Remarks:

1. Allow the student to attempt think through the program first, by asking them how they are thinking of approaching it and letting them talk out their reasoning.

2. Encourage the student to approach the problem in steps that they understand; print out the question, then read in the user's input, then add the if statement to check if that answer is correct or not.

3. Have the studend add the tries and scoring after they've written a functining quiz first. 

"""

tries = 0
score = 0

print("Who was the second president of the United States.")
print("a) George Washington")
print("b) Abraham Lincoln")
print("c) Thomas Jefferson")
print("d) John Adams")

answer = input()
tries = tries + 1

if answer == "d" or answer == "D" or answer == "John Adams":
  score = score + 1
  print("Correct! You have answered", score, "out of", str(tries) + ".")
else:
  print("Incorrect! You have answered", score, "out of", str(tries) + ".")
print()

print("Who was the sixteenth president of the United States.")
print("a) George Washington")
print("b) Abraham Lincoln")
print("c) Thomas Jefferson")
print("d) John Adams")

answer = input()
tries = tries + 1

if answer == "b" or answer == "B" or answer == "Abraham Lincoln":
  score = score + 1
  print("Correct! You have answered", score, "out of", str(tries) + ".")
else:
  print("Incorrect! You have answered", score, "out of", str(tries) + ".")
print()

print("Who was the first president of the United States.")
print("a) George Washington")
print("b) Abraham Lincoln")
print("c) Thomas Jefferson")
print("d) John Adams")

answer = input()
tries = tries + 1

if answer == "a" or answer == "A" or answer == "George Washington":
  score = score + 1
  print("Correct! You have answered", score, "out of", str(tries) + ".")
else:
  print("Incorrect! You have answered", score, "out of", str(tries) + ".")
print()

print("Who was the third president of the United States.")
print("a) George Washington")
print("b) Abraham Lincoln")
print("c) Thomas Jefferson")
print("d) John Adams")

answer = input()
tries = tries + 1

if answer == "c" or answer == "C" or answer == "Thomas Jefferson":
  score = score + 1
  print("Correct! You have answered", score, "out of", str(tries) + ".")
else:
  print("Incorrect! You have answered", score, "out of", str(tries) + ".")
print()

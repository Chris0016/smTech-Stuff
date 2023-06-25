# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 1.3.2                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal: Teach the basic arithmetic operators. Further practice using if statements.

Remarks:


"""

x = int(input("Enter the first operand. "))
y = int(input("Enter the second operand. "))

op = input("Enter the operation. ")

if op == "add" or op == "+":
  print(x + y)

if op == "sub" or op == "-":
  print(x - y)

if op == "mul" or op == "*":
  print(x * y)

if op == "div" or op == "/":
  print(x / y)

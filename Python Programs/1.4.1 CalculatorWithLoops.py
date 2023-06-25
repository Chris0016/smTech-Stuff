# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Brin Brody           #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 1.4.1                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal: Reinforce the concept of while loops.

Remarks:

1. 


"""

runAgain = True

#Not necessary to compare against True,
#but it's a good idea to explicitly do this
#to keep things clear for the student.

while runAgain == True:
    oper = input("Enter an operation: ")
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    
    if oper == "+":
        print(num1 + num2)
    elif oper == "-":
        print(num1 - num2)
    elif oper == "*":
        print(num1 * num2)
    elif oper == "/":
        print(num1 / num2)
    else:
        print("Invalid operation.")
        
    again = input("Complete another calculation? (y/n): ")
    if again == "n":
        runAgain = False

# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Brin Brody           #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 3.0.3                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

runAgain = True

while runAgain == True:
    oper = input("Enter an operation: ")
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    if(oper == "+"):
        print(add(num1, num2))
    elif oper == "-":
        print(subtract(num1, num2))
    elif oper == "*":
        print(multiply(num1, num2))
    elif oper == "/":
        print(divide(num1, num2))
    else:
        print("Invalid operation.")

    again = input("Complete another calculation? (y/n): ")
    if again == "n":
        runAgain = False

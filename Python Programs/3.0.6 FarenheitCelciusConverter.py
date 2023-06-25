# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Brin Brody           #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 3.0.6                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

def farenheitToCelcius(temp):
    return (temp - 32) * (5/9)

def celciusToFarenheit(temp):
    return temp * (9/5) + 32

runAgain = True

while runAgain == True:
    unit = input("Original Value Unit? (F/C): ")
    temp = int(input("Temperature in Degrees " + unit + ": "))
    
    if unit == "F":
        print(temp, "degrees Celcius is equal to",celciusToFarenheit(temp), "degrees Farenheit.")
    elif unit == "C":
        print(temp, "degrees Farenheit is equal to",farenheitToCelcius(temp), "degrees Celcius.")
    else:
        print("Invalid Unit of Temperature")

    again = input("Complete another conversion? (y/n): ")
    if again == "n":
        runAgain = False

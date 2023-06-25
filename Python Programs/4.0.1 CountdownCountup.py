# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Jared Okun           #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 4.0.1                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

def countDown(x):
    if x >= 0:
        print(x)
        countDown(x - 1)

def countUp(start, end):
    if start <= end:
        print(start)
        countUp(start + 1, end)

countDown(10)
countDown(-1)

countUp(2, 5)
countUp(6, 5)

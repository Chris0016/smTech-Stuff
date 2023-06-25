# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Jared Okun           #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 4.0.5                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

def exp(a, b):
    if b == 0:
        return 1
    return exp(a, b - 1) * a

print(exp(4, 3))

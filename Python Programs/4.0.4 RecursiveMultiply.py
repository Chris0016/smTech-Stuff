# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Jared Okun           #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 4.0.4                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

def mul(a, b):
    if b == 0:
        return 0
    return mul(a, b - 1) + a

print(mul(3, 11))

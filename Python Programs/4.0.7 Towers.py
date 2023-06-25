# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Jared Okun           #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 4.0.7                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED


def towers(disk, start, mid, end):
  
  if(disk > 0):
    towers(disk-1, start, end, mid)
    print("Move disk", disk, "from peg" , start, "to peg", end)
    towers(disk-1, mid, start, end)

towers(7, 1, 2, 3)

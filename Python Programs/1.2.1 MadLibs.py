# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 1.2.1                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes

Goal: To reinforce the students understanding of printing, variables, and input. To have a student solve a problem that involves several lines of code.

Remarks:

1. Students may be unfamiliar with the mad libs game or the different parts of speech. Be sure to explain the game and provide an example if the student is unfamiliar with it, and relax the part of speech requirements if students are struggling with it.

2. If a student is stuck on making the mad libs program, have them write a simple story in a text editor. Next, suggest some words for them to remove and replace with blanks. Finally, move the story into a print/output statement in their actual program.

3. A good rule of thumb is 3-5 parts of speech.


"""

name = input("Please enter in a name. ")
verb = input("Please enter in an infinitive verb (i.e. to walk, to sing). ")
object = input("Please enter in an object. ")
adjective = input("Please enter in an adjective. ")
sound = input("Please enter in a sound. ")

print(name, "really liked", verb, "in the park. One day he was walking there when a(n)", adjective, object, "fell out of the sky and hit him on the head with a", sound + ".", "That was the last time", name, "went to that park.")

"""
Challenge: 

For older or more knowledgeable students, consider doing a version of this program that puts together a simple html page. Query the user for simple information and then print out that information between html elements.

"""

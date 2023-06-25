# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 6.0.4                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Teaching Notes:

Goal: Utilize data structures to solve problems. Put both Linked Lists and Stacks in a practical context.

1. Walk through, visually and verbally, the process of evaluating a postfix expression with a stack.
  - If token is a number, push it on the stack
  - If token is an operator:
    i) pop two elements from the stack
    ii) compute the result
    iii) push the result back on the stack
  - repeat until the input is exhausted, (the number left on the stack is the result)

2. Try and let the student think through how to solve the problem on their own first. When they need help, guide them by breaking the problem down into steps.
  - Reading in the input from the user.
  - Splitting the input into separate 'tokens'.
  - Write a method to identify operators for convenience and clarity [optional but recommended]
  - Use a stack to evaluate the token list and compute the result.
  
3. Introduces isspace() for identifying whitespace in a string if a student has not seen it before.

4. This method of parsing the string is relatively inefficient and unwieldy to write as well as requires strict formatting of what the user inputs. A more robust approach would be to use a regular expression. This is presented as an extension below.

"""

def isOperator(x):
  if (x == "+"):
    return True
  elif (x == "-"):
    return True
  elif (x == "*"):
    return True
  elif (x == "/"):
    return True
  else:
    return False

def evaluate(x, y, operator):
  if (operator == "+"):
    return x + y
  elif (operator == "-"):
    return x - y
  elif (operator == "*"):
    return x * y
  elif (operator == "/"):
    return x / y

from Stack import Stack

stack = Stack()

expression = input("Please enter an expression (separated by spaces) into the calculator in postfix notation i.e. 2 + 2 * 3 would be 2 2 3 * +\n")

#Parse the string into its separate pieces
result = ""
tokens = []
for i in expression:
  if (i.isspace()):
    if (result != ""):
      tokens.append(result)
    result = ""
  else:
    result += i

#Catch the last token that may or may not have had a space after it
if (result != ""):
  tokens.append(result)


#Finally, use a stack to evaluate the expression
for i in tokens:
  if (not isOperator(i)):
    stack.push(float(i)) #If the token is a number, convert it to a double and push it on the stack
  else:
    rvalue = stack.pop()
    lvalue = stack.pop()
    result = evaluate(lvalue, rvalue, i)
    stack.push(result)

#Print out the final answer
print(stack.pop())

"""
Extension:

1. If a user enters an invalid expression like "2 +" or "2 2 + +", the program will run into an error when it tries to pop two values from the stack to compute the final operation. Extend the program to identify this situation, give a useful message to the user, and exit without crashing. Can it handle an empty string ""?

2. Tokenize the user's expression using split (and optionally strip). Possible solutions are provided below.

#Explicitly using the regular expression
import re
tokens = re.split("\s+", expression.strip())

#Using the default behavior of python's string split
tokens = expression.split()
  
"""

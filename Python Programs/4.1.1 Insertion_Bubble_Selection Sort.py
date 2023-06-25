# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 4.1.1                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

# Note: Try and let the student come up with an idea for how to sort, and then match what they
#       come up with to one of these sorting strategies. The majority of students come up with
#       something along the lines of bubble sort or selection sort.
#
# Note 2: Do not have students do all three at once, unless you're working with an advanced student
#         who expresses an interest. This can be something to revisit later on for more practice.

from random import randint

def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-1):
      if arr[j] > arr[j + 1]:
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp

def selectionSort(arr):
  smallest = 0

  for i in range(len(arr)):
    for j in range(i, len(arr)):
      if arr[j] < arr[smallest]:
        smallest = j

    temp = arr[i]
    arr[i] = arr[smallest]
    arr[smallest] = temp

    smallest = i + 1

def insertionSort(arr):
  for i in range(1, len(arr)):
    j = i
    while j > 0 and arr[j-1] > arr[j]:
      temp = arr[j-1]
      arr[j-1] = arr[j]
      arr[j] = temp

      j = j - 1


sampleArray = []

for i in range(8):
  sampleArray.append(randint(0, 100))

print("Bubble Sort:")
print(sampleArray)
bubbleSort(sampleArray)
print(sampleArray)

sampleArray = []

for i in range(8):
  sampleArray.append(randint(0, 100))

print()
print("Selection Sort:")
print(sampleArray)
selectionSort(sampleArray)
print(sampleArray)

sampleArray = []

for i in range(8):
  sampleArray.append(randint(0, 100))

print()
print("Insertion Sort:")
print(sampleArray)
insertionSort(sampleArray)
print(sampleArray)


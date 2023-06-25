# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 4.1.3                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

"""
Quick Sort can be very tricky for students (and teachers). 

Guideline for teaching: 
1. Give a visual walkthrough of how Quicksort sorts an array.
2. Break it into the logical steps-
  - Select a pivot
  - Partition the array
  - Quick Sort both sides
3. When the student's code doesn't work, (it probably won't),
   visually walk through what happens when an array of size 0, 1, 2, 3, and n
   is sorted. 
   
If a student is truly stuck on the "in-place" quicksort, they can
do the quick sort with extra lists.

A quick and easy method, checkSorted, can be useful for rapidly checking
how well the quickSort performed on larger arrays. Using larger array sizes
helps identify any issues in the corner cases of quicksort.
"""

from random import randint

def quickSort(arr, left, right):
  
  if (right-left == 1):
    if (arr[right] < arr[left]):
      temp = arr[left]
      arr[left] = arr[right]
      arr[right] = temp
    return
  elif (right-left < 1):
    return
  else:
    p = randint(left, right)
    p = partition(arr, left, right, p)

    quickSort(arr, left, p - 1)
    quickSort(arr, p + 1, right)


def partition(arr, left, right, p):
  #Swap pivot into leftmost position, update positions
  pivot = arr[p]
  arr[p] = arr[left]
  arr[left] = pivot
  p = left
  left += 1
  
  #Partition
  while (left != right):
    while(arr[left] <= pivot and left != right):
      left += 1
    while(arr[right] > pivot and left != right):
      right -= 1

    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

  #Swap the pivot into place
  if (arr[left] > pivot):
    temp = arr[left - 1]
    arr[left - 1] = pivot
    arr[p] = temp

    return left - 1
  else:
    temp = arr[left]
    arr[left] = pivot
    arr[p] = temp

    return left

def checkSorted(arr):
  for i in range(len(arr) - 1):
    if (arr[i] > arr[i + 1]):
      return False
  return True

arr = []
for i in range(100):
  arr.append(randint(1, 1000))

print(arr)

quickSort(arr, 0, len(arr) - 1)

print(arr)

if (checkSorted(arr) == True):
  print("Sorted!")
else:
  print("Not sorted!")

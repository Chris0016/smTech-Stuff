# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Matthew Baptist      #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 4.1.2                    #
# - - - - - - - - - - - - - - - - #

#SUMMERTECH CONFIDENTIAL
#COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED

from random import randint

def merge(arr, left, right):
  mid = (left + right) // 2
  sorted = []

  i = left
  j = mid + 1

  #Take from the left or right subarrays until we reach the end of one
  while i < mid + 1 and j < right + 1:
    if arr[i] <= arr[j]:
      sorted.append(arr[i])
      i = i + 1
    else:
      sorted.append(arr[j])
      j = j + 1

  while j < right + 1:
    sorted.append(arr[j])
    j = j + 1

  while i < mid + 1:
    sorted.append(arr[i])
    i = i + 1

  #Copy over the results
  for k in range(len(sorted)):
    arr[left + k] = sorted[k]

def mergeSort(arr, left, right):
  mid = (left + right) // 2

  if (right - left) == 0:
      return
  else:
    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merge(arr, left, right)

sampleArray = []

for i in range(15):
  sampleArray.append(randint(0, 100))

print(sampleArray)
mergeSort(sampleArray, 0, len(sampleArray)-1)
print(sampleArray)

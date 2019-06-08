# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 00:30:33 2019

HackerRank --
Practice > Interview Preparation Kit > Arrays ---> Minimum Swaps 2

@author: moorem24
"""


arr = [1,3,5,2,4,6,7]
n = len(arr)


# find start of consecutive numbers - this will be the array position offset
# not necessary --- all sets start with 1
#offset = None
#for i in range(n-1):
#    if i == 0:
#        offset = arr[i]
#    elif arr[i] < offset:
#        offset = arr[i]

### this solution times out for large test cases due to O(n^2) time of nested loop --- WORKS IN JAVA
# execute swaps (from left to right switch out of order int with the correct int for that position) and count them
offset = 1
swapcount = 0
for i in range(n):
    if arr[i] != i + offset:
        for j in range(i, n):
            if arr[j] == i + offset:
                arr[i], arr[j] = arr[j], arr[i]
                swapcount += 1
                break         
print(swapcount)      


### this doesn't work - logical error
#count = 0
#for i in range(n):
#    if (arr[i] != i + 1) and (arr[i] < arr[arr[i]-1]):
#        arr[i], arr[arr[i] - 1] = arr[arr[i] - 1], arr[i]
#        print("swapping", arr[i], " and ", arr[arr[i] -1])
#        count += 1
#
#print(count)  


### doesn't work, logical error
#left = 0
#right = len(arr) -1
#minswaps = 0
#while left < right:
#    while (arr[left] == left + 1) and (left < right):
#        left += 1
#    if (left < right) :
#       arr[i], arr[arr[i] - 1] = arr[arr[i] - 1], arr[i]
#       minswaps += 1
#    left += 1
#   
#print(minswaps)


        
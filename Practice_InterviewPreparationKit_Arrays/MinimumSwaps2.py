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
offset = None
for i in range(n-1):
    if i == 0:
        offset = arr[i]
    elif arr[i] < offset:
        offset = arr[i]

# execute swaps (from left to right switch out of order int with the correct int for that position) and count them
swapcount = 0
for i in range(n):
    if arr[i] != i + offset:
        for j in range(i, n):
            if arr[j] == i + offset:
                arr[i], arr[j] = arr[j], arr[i]
                swapcount += 1
            
print(swapcount)            

        
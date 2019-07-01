# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 00:59:12 2019

HackerRank --
Practice > Interview Preparation Kit > Hash Tables ---> Count Triplets

@author: moorem24
"""

n = 5
r = 2
arr = [1, 2, 1, 2, 4]


count = 0
for i in range(len(arr) - 2):
    for j in range(i+1, len(arr) - 1):
        print(int(arr[j] / r))
        if arr[j] / r == arr[i]:
            for k in range(j + 1, len(arr)):
                if int(arr[k] / r) == arr[j]:
                    count += 1
              
print(count)                
print(count)
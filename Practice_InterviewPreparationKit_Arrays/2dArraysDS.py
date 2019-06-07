# -*- coding: utf-8 -*-
"""
Spyder Editor

HackerRank --
Practice > Interview Preparation Kit > Arrays ---> 2D Array DS

This is a temporary script file.
"""


import math
import os
import random
import re
import sys





# Complete the hourglassSum function below.
def hourglassSum(arr):
    
#    hgSums = []         # used to test
    temp = 0
    maxSum = None


    for i in range(4):
        for j in range(4):
            temp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
#           hgSums.append(temp)   # used to test
            if (i == 0) and (j == 0):
                maxSum = temp
            else:
                if temp > maxSum:
                    maxSum = temp

    return maxSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:47:16 2019

HackerRank --
Practice > Interview Preparation Kit > Warm-up Challenges ---> Repeated String

@author: moorem24
"""

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    
    baseNumA = 0
    remNumA = 0
    divisBy = math.floor(n / len(s))

    for i in range(len(s)):
        if s[i] == 'a':
            baseNumA += 1
            if i < (n % len(s)):
                remNumA += 1


    countA = (divisBy * baseNumA) + remNumA
    return countA

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

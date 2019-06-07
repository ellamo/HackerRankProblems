# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 00:01:55 2019

HackerRank --
Practice > Interview Preparation Kit > Warm-up Challenges ---> Jumping on the Clouds

@author: moorem24
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0

    i = 0
    n = len(c)
    while i < (n - 1):
        if (i < (n - 2)) and (c[i + 2] == 0):
            i += 2
            jumps += 1
        elif c[i + 1] == 0:
            i += 1
            jumps += 1
        else:
            i = n
    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

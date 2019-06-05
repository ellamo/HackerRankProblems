# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:04:39 2019

HackerRank --
Practice > Interview Preparation Kit > Warm-up Challenges ---> Sock Merchant

@author: moorem24
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sortflag = True
    while sortflag:
        temp = 1
        sortflag = False 
        for i in range(n-1):
            if ar[i] > ar[i+1]:
                temp = ar[i+1]
                ar[i+1] = ar[i]
                ar[i] = temp
                sortflag = True

    pairs = 0
    skipflag = False
    for i in range(n-1):
        if not skipflag:
            if ar[i] == ar[i+1]:
                pairs += 1
                skipflag = True
        else:
            skipflag = False

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 23:21:05 2019

HackerRank --
Practice > Interview Preparation Kit > Hash Tables ---> Sherlock and Anagrams

@author: moorem24
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    d = collections.defaultdict(int)
    
    # add all sorted substrings to the dictionary and count each occurrence
    for i in range(len(s)):
        for j in range (i + 1, len(s) + 1):    # adding one offsets right of slice
            d[ ''.join(sorted(s[i:j])) ] += 1
    
    count = 0
    # compute the combinations of each substring with more than 1 occurrence and sum all combinations
    for el in d:
        if d[el] > 1:
            count += int( math.factorial(d[el]) / (2 * math.factorial(d[el] - 2)) )

    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

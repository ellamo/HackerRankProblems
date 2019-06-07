# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:17:02 2019

HackerRank --
Practice > Interview Preparation Kit > Warm-up Challenges ---> Counting Valleys

@author: moorem24
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    altitude = 0
    valleys = 0
    
    for i in range(n):
        if s[i] == "D":
            altitude -= 1
        else:
            altitude += 1
            if (altitude == 0):
                valleys += 1
                valleyEntered = False

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

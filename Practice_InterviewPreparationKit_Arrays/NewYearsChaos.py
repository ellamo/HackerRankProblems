# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:22:30 2019

HackerRank --
Practice > Interview Preparation Kit > Arrays ---> New Years Chaos

@author: moorem24
"""

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

    errorflag = False
    moves = 0

    for i in range(len(q)):
        if q[i] > (i + 3):
            errorflag = True
            break
        
    
    if errorflag:
        print("Too chaotic")
    else:

        # bubblesort to reverse moves
        swapflag = True
        while swapflag:
            swapflag = False

            for i in range(len(q) - 1):
                if q[i] > q[i+1]:
                    q[i], q[i+1] = q[i+1], q[i]
                    moves += 1
                    swapflag = True

        print(moves)

        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

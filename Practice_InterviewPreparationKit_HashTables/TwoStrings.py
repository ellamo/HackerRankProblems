# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 22:29:49 2019

HackerRank --
Practice > Interview Preparation Kit > Hash Tables ---> Two Strings

@author: moorem24
"""




''' SOLUTION USING EXCEPTION HANDLING '''
###############################################################################
import math
import os
import random
import re
import sys


def twoStrings(s1, s2):
    d1 = {el:1 for el in s1}
    d2 = {el:1 for el in s2}
    
    subFound = False
    if len(d1) < len(d2):
        for el in d1:       
            try:
                if d2[el] > 0:
                    subFound = True
                    break
            except:
                pass
    else:
        for el in d2:
            try:
                if d1[el] > 0:
                    subFound = True
                    break
            except:
                pass
            
    if subFound:
        return "YES"
    else:
        return "NO"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

###############################################################################






''' SOLUTION USING COLLECTIONS LIBRARY '''
###############################################################################
import math
import os
import random
import re
import sys
import collections



# Complete the twoStrings function below.
def twoStrings(s1, s2):
    dict1 = collections.Counter(s1)
    dict2 = collections.Counter(s2)

    subFound = False
    if len(dict1) < len(dict2):
        for el in dict1:
            if dict2[el] > 0:
                subFound = True
                break
    else:
        for el in dict2:
            if dict1[el] > 0:
                subFound = True
                break
    
    if subFound:
        return "YES"
    else:
        return "NO"
    
    
     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

###############################################################################
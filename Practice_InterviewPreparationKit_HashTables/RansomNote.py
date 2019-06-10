# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 00:30:33 2019

HackerRank --
Practice > Interview Preparation Kit > Hash Tables ---> Ransom Note

@author: moorem24
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dictMag = {e:0 for e in magazine}
    for el in magazine:
        dictMag[el] += 1

    valid = True

    try:
        for el in note:
            if dictMag[el] == 0:
                valid = False
            else:
                dictMag[el] -= 1
            
        if valid:
            print("Yes")
        else:
            print("No")
    except:
        print("No")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

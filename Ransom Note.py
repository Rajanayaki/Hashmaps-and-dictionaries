#!/bin/python3
#hackerrank solution
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dic={}
    noteidx=0
    magidx=0
    for word in note:
        if word not in dic:
            dic[word]=1
        else: 
            dic[word]+=1
    for word in magazine:
        if word in dic:
            dic[word]-=1
    for i,j in dic.items():
        if j>0:
            print("No")
            sys.exit()
        
    print("Yes") 
    
    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

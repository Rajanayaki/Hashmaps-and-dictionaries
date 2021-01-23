#!/bin/python3
#hackerrank solution
import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):              
    dic1=[0]*26
    dic2=[0]*26
    flag=0
    for i in s1: 
        dic1[ord(i)-ord('a')]=1
    for i in s2:
        dic2[ord(i)-ord('a')]=1
    for i in range(0,26):
        if dic1[i] and dic2[i]:
            return "YES"
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

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    brides = 0
    for i in range(len(q)-1,0,-1):
        if(q[i] == i+1):
            continue
        elif(q[i-1] == i+1):
            brides += 1
            q[i],q[i-1] = q[i-1],q[i]
        elif(q[i-2] == (i+1)):
            brides += 2
            q[i-1],q[i-2] = q[i-2],q[i-1]
            q[i],q[i-1] = q[i-1],q[i]
        else:
            print("Too chaotic") 
            return
    print(brides)     
    return

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n_pos = 0
    n_zero = 0
    n_neg = 0
    len_num = 0
    for number in arr:
        if(number < 0):
            n_neg += 1
        elif(number == 0):
            n_zero += 1
        else:
            n_pos += 1
        len_num += 1
    print(round(n_pos/len_num,6))
    print(round(n_neg/len_num,6))
    print(round(n_zero/len_num,6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
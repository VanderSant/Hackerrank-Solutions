#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.copy()
    arr.sort()
    len_arr = len(arr)
    min = sum(arr[0:4])
    max = sum(arr[len_arr-4:len_arr])
    print('{min} {max}'.format(min = min,max = max))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

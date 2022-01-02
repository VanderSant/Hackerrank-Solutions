#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#
# I need to improve that yet, note:70/100

def find_index(A,value):
    index = 0
    len_a = len(A)
    if(len_a == 0):
        return 0
    if(A[len_a-1]<=value):
        return len_a 
    for i in range(len_a):
        if(A[i]>=value):
            return i
        else:
            continue
           
def cookies(k, A):
    len_A = len(A)
    A.sort()
    operations = 0
    while(A[0]<k):
        if(len_A<=1):
            return -1
        new_value = 1*A[0] + 2*A[1]
        A.pop(0)
        A.pop(0)
        A.insert(find_index(A,new_value),new_value)
        operations += 1
        len_A -= 1
    return operations
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
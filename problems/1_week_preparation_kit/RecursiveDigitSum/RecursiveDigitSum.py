#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    if((len(n) == 1)and(k>1)):
        n,k = str(int(n)*k),1
    len_n = len(n) 
    if(len_n==1):
        return (int(n))
    else:
        suma = 0
        isImp = len_n%2
        for i in range(0,int((len_n/2))+isImp):
            pos_f = i
            pos_b = len_n-i-1
            if(pos_f != pos_b):
                suma += (int(n[pos_f])+int(n[pos_b]))
            else:
                suma += int(n[pos_f])
        return superDigit(str(suma),k)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
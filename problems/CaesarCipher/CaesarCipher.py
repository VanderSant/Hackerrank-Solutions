#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    list_s = []
    if (k>26):
        k = k%26
    for i,char in enumerate(s):
        if((ord(char)>=97)and(ord(char)<=122)):  
            new_char = ord(char)+k
            if(new_char>122):
                new_char -=26
            list_s.append(chr(new_char))
        elif((ord(char)>=65)and(ord(char)<=90)):
            new_char = ord(char)+k
            if(new_char>90):
                new_char -=26
            list_s.append(chr(new_char))
        else:
            list_s.append(s[i])
    new_string = ''.join(list_s)
    return new_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
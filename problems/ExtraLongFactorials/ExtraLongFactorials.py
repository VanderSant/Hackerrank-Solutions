#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    result = 1
    for i in range(0,n):
        result = result * (n-i)
        
    
    print(result)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
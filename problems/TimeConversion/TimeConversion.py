#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    len_s = len(s)
    data_h = s[0:2]
    time_format = s[len_s-2:len_s]
    if((time_format == "PM") and (data_h != "12")):
        data_h = str(int(data_h)+12)
    elif((time_format == "AM") and (data_h == "12")):
        data_h = "00"        
    s = data_h+s[2:]
    s = s[0:len_s-2]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')
    
    fptr.close()
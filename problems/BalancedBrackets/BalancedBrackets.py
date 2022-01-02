#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
bracket_compl = lambda s: '}' if s=='{' else ']' if s=='[' else ')' if s=='(' else None #'{' if s=='}' else '[' if s==']' else '(' if s==')' else 'a'

bracket_compl_inv = lambda s: '{' if s=='}' else '[' if s==']' else '(' if s==')' else None

def isBalancedRecursive(s):
    new_bracket = []
    for s_i in s:
        if(bracket_compl(s_i) != None):
            new_bracket.append(s_i)
        else:
            if((len(new_bracket)>0) and (bracket_compl_inv(s_i) == new_bracket[-1])):
                new_bracket.pop()
            else:
                return False
    if(len(new_bracket) == 0):
        return True
    else:
        return False
    
def isBalanced(s):
    if(isBalancedRecursive(s) == True):
        return "YES"
    else:
        return "NO"  
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

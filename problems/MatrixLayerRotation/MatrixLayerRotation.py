#!/bin/python3

import math
import os
import random
import re
import sys
import copy

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def rotate_matrix(matrix,c):
    s = len(matrix)
    n = len(matrix[0])
    new_matrix = copy.deepcopy(matrix)

    new_range = [value[c:n-c] for value in new_matrix[c:s-c]]
    new_range_s = len(new_range) -1
    new_range_n = len(new_range[0]) -1

    for i in range(new_range_s):
        new_matrix[c+i+1][c] = matrix[c+i][c]
        
    for i in range(new_range_n):
        new_matrix[s-c-1][c+i+1] = matrix[s-c-1][c+i]
        
    for i in range(new_range_s):
        new_matrix[s-c-i-2][n-c-1] = matrix[s-c-i-1][n-c-1]
        
    for i in range(new_range_n):
        new_matrix[c][n-c-i-2] = matrix[c][n-c-i-1]
    
    return new_matrix

def matrixRotation(matrix, r):
    # Write your code here
    s = len(matrix)
    n = len(matrix[0])

    new_matrix = matrix
    for c in range(s):
        for _ in range(r): 
            new_matrix = rotate_matrix(new_matrix, c)
        
        new_range = [value[c:n-c] for value in new_matrix[c:s-c]]
        new_range_s = len(new_range) -1
        new_range_n = len(new_range[0]) -1

        if (new_range_s <= 2 or new_range_n <= 2):
            break

    string_p = ""
    for i in range(s):
        for j in range(n):
            string_p += str(new_matrix[i][j]) + " "
        string_p += "\n"
        
    print(string_p)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)

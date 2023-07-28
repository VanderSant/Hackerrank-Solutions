#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Acredito que fazer  uma busca binaria deixaria o algoritmo bem mais rapido
    ranked_with_no_repeted_values = sorted(list(set(ranked)), reverse=True)
    result = []
    for current_points in player:
        current_position = 1
        for position_point in ranked_with_no_repeted_values:
            if current_points < position_point:
                current_position += 1
            else:
                ranked_with_no_repeted_values = ranked_with_no_repeted_values[0:current_position]
                break
        result.append(current_position)
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

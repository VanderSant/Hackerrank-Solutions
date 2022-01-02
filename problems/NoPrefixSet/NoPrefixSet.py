#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#
    
def noPrefix(words):
    validated_words,validated_chars = set(),set()
    for word in words:
        if(word in validated_chars):
            print("BAD SET")
            return print(word)
        else:
            validation = ''
            for char in word:
                validation += char
                validated_chars.add(validation)
                if(validation in validated_words):
                    print("BAD SET")
                    return print(word)
        validated_words.add(word)
        
    return print("GOOD SET")

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)

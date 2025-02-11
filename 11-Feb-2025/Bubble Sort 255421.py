# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                count+=1
    
    return count

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    swaped= countSwaps(a)
    print("Array is sorted in " + f'{swaped}'+" swaps." )
    print("First Element: " + f'{a[0]}')
    print("Last Element: " + f'{a[-1]}')

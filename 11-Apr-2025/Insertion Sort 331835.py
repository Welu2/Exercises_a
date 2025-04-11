# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    current = arr[n -1]
    for i in range(n - 2, -1, -1):
        if current > arr[i]:
            arr[i + 1] = current
            print(*arr) 
            break
        elif current < arr[i]:
            arr[i + 1] = arr[i]
            print(*arr)
        elif current == arr[i]:
            arr[i+1] = current
            print(*arr)
            break
            
    
    if current < arr[0]:
        arr[0]=current
        print(*arr)    

if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

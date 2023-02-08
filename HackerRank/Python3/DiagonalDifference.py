#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    mat = len(arr[0]) #type of matrix e.g(3by3)
    left_sum = 0
    right_sum =0
    k = mat-1 #rightmost element accessor 

    for i in range(mat):
        left_sum += arr[i][i] 

    for j in range(mat):
        right_sum += arr[j][k]
        k-=1

    return abs(right_sum - left_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
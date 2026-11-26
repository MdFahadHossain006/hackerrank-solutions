# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true
# Problem     2D Array - DS
# Difficulty  Easy
# Subdomain   Arrays
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-26, 09:29 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    max_sum = -float('inf')

    for r in range(4):
        for c in range(4):
            current_sum = (
                arr[r][c] + arr[r][c + 1] + arr[r][c + 2]
                + arr[r + 1][c + 1]
                + arr[r + 2][c] + arr[r + 2][c + 1] + arr[r + 2][c + 2]
            )
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

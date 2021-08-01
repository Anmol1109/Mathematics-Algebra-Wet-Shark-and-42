#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER s as parameter.
#

a = 1000000007

def solve(s):
    return ((s * 21 - 1) // 20 * 2) % a
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = int(input().strip())

        result = solve(s)

        fptr.write(str(result) + '\n')

    fptr.close()

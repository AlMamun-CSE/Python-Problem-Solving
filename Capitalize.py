#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(line):
    return ' '.join(s[:1].upper() + s[1:] for s in line.split(' '))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
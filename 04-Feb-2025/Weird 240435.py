# Problem: Weird - https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

def conds(n):
    if n % 2 != 0:
        print ("Weird")
    elif n % 2 == 0 and n in range(2,5):
        print ("Not Weird")
    elif n % 2 == 0 and n in range(6,21):
        print ("Weird")
    elif n % 2 == 0 and n > 20:
        print ("Not Weird")    

if __name__ == '__main__':
    n = int(input().strip())
    conds(n)

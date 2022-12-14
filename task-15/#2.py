#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a,b=0,1
    sum=0
    while a < n :
        if a % 2 == 0:
            sum+=a
        a,b = b, a+b
    print(sum)
            
        
#!/bin/python3

import sys


t = int(input().strip())
ans=[]
for a0 in range(t):
    n = int(input().strip())
    i=2
    while i < n :
        if n%i == 0 :
            n = n / i
            i=2
        else:
            i+=1
    ans.append(i)
for k in ans:
    print(k)


                    

            
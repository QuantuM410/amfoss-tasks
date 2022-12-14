#!/bin/python3

import sys


t = int(input().strip())
ans=[]
for a0 in range(t):
    n = int(input().strip())
    f=[]
    for i in range(100,n):
        for j in range(100,n):
            pro= i*j
            if str(pro) == str(pro)[::-1]:
                f.append(pro)
    ans.append(max(f))
for k in ans:
    print(k)
    
            
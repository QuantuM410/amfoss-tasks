import sys


t = int(input().strip())
ans=[]
for a0 in range(t):
    n = int(input().strip())
    sum=0
    for j in range(n):
        if j%3 == 0 or j%5 == 0 :
            sum+=j
    ans.append(sum)
for k in ans:
    print(k)
t=int(input())
ans=[]
for group in range(t):
    nummonster=int(input())
    a=input().split()
    hpmonster=[]
    for i in a:
        hpmonster.append(int(i))
    for k in range(len(hpmonster)+1):
        for i in range(len(hpmonster)-1):
            if hpmonster[i+1]-hpmonster[i] >= 0:
                hpmonster[i+1]=hpmonster[i+1]-hpmonster[i]
        while 0 in hpmonster:   
            hpmonster.remove(0)
    if len(hpmonster) == 1 or len(hpmonster) == 0 :
        ans.append('YES')
    else :
        ans.append('NO')
for y in ans:
    print(y)



    
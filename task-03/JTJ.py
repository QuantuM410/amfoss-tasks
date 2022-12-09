t=int(input())
ans=[]
for case in range(t):
    x=int(input())
    a,b,c=map(int, input().split())
    portal=[a,b,c]
    n=0
    for i in range(3):
        if portal[x-1] == 0 and n<2:
            ans.append('NO')
            break
        else:
            proxy=x
            x=portal[x-1]
            portal[proxy-1]=0
            n+=1
        if portal == [0,0,0] and n == 3:
            ans.append('YES')
            break
for j in ans:
    print(j)

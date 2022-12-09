t=int(input())
cou=0
ans=[]
for city in range(t):
    n=int(input())
    a=input().split()
    while(True):
        mana=0 
        c=[]
        for i in a :
            c.append(int(i))
        c.sort()
        Ocount=0
        for p in c:
            if p == 0:
                Ocount+=1
        if Ocount!=0:
            mana=len(c)-Ocount
            ans.append(mana)
            break
        duplicacy=0
        for i in range(len(c)-1):
            if c[i] == c[i+1]:
                duplicacy+=1
                k=i
        
        if duplicacy!=0 :
            c[k]=0
            mana+=len(c)
            ans.append(mana)
            break
        else :
            mana+=(len(c)+1)
            ans.append(mana)
            break
for f in ans:
    print(f)
        


    

    
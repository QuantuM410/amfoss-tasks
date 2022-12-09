n,m=map(int, input().split())
words=[]
for i in range(m):
    word=input().split()
    words.append(word)
spell=input().split()
ans=[]
for i in range(len(spell)):
    for j in words:
        if spell[i] in j :
            if len(j[0]) > len(j[1]) :
                ans.append(j[1])
            
            if len(j[0]) < len(j[1]) :
                ans.append(j[0])

            if len(j[0]) == len(j[1]) :
                ans.append(j[0])
for l in ans:
    print(l,'', end='')
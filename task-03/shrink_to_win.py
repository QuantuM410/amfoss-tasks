n=int(input())
sum=0
counter=1
while (n>0 or sum>9):
    if n==0 :
        n=sum
        sum=0
        counter+=1
        
    sum=sum+(n%10)
    n=n//10
    
print(counter)



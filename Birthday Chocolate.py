n=int(input())
bar=list(map(int,input().split()))
d,m=map(int,input().split())
case=0

for i in range(n-m+1):
    sum1=0
    count=0
    while count!=m:
        sum1=sum1 + bar[i+count]
        count+=1
        
    if (sum1==d):
        case=case+1
    
print(case)

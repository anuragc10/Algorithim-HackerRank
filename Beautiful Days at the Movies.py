i,j,k=map(int,input().split())

count=0
for p in range(i,j+1):
    n=(str(p)[::-1])
    if(abs(p-int(n))%k==0):
        count+=1
print(count)

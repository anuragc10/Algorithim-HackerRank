n=int(input())
c=list(map(int,input().split()))
ans=0
i=0

while i<n-1:
    if(i+2>=n or c[i+2]==1):
        i=i+1
        ans=ans+1
    else:
        i=i+2
        ans=ans+1
print(ans)


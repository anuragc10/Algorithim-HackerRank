t=int(input())


for i in range(t):
    c=0
    j=0
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    for j in arr:
        if(j<=0):
            c+=1
    if(c>=k):
        print("NO")
    else:
        print("YES")
    arr.clear()

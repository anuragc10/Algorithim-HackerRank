n=int(input())
arr=list(map(int,input().split()))
arr.sort()
a=0

for i in range(n):
    for j in range(n):
        if(abs(arr[j]-arr[i])<=1):
            a=max(a,j-i+1)
print(a)
    

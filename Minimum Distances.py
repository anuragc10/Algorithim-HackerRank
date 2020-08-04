n=int(input())
arr=list(map(int,input().split()))
arr1=list()
a=10000001
for i in range(n):
    for j in range(n):
        if(arr[i]==arr[j] and i!=j):
            a=min(a,abs(i-j))

if(a==10000001):
    a=-1
print(a)

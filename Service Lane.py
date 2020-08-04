n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr1=list()


for i in range(m):
    p,q=map(int,input().split())
    arr1=arr[p:q+1]
    print(min(arr1))
    

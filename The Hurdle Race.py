n,k=map(int,input().split())
arr=list(map(int,input().split()))
p=set(arr)
q=list(p)
q.sort(reverse=True)

if(q[0]>k):
    print(q[0]-k)
else:
    print("0")

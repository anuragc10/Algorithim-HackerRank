import math
n=int(input())

for i in range(n):
    count=0
    a,b=map(int,input().split())
    for j in range(a,b+1):
        root=0
        root = math.sqrt(j)
        if int(root + 0.5) ** 2 == j:
            count+=1
        else:
            continue
    print(count)


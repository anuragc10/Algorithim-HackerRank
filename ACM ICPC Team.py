n,m=map(int,input().split())
arr=list()
for p in range(n):
    k=input()
    arr.append(k)

count=0

count1=list()


for i in range(n):
    for j in range(i+1,n):
        count=0
        for k in range(m):
            if(int(arr[i][k])==1 or int(arr[j][k])==1):
                count=count+1
        count1.append(count)


print(max(count1))
print(count1.count(max(count1)))



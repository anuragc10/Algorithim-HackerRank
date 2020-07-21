n=int(input())
ar=list(map(int,input().split()))
ar.sort()
set1=sorted(set(ar))
lst=list()

for i in set1:
    lst.append(ar.count(i))


for j in range(len(lst)):
    lst[j]=int(lst[j]/2)
print(sum(lst))

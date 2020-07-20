n=int(input())
arr=list(map(int,input().split()))
arr.sort()
lst=list()

for i in range(1,6):
    lst.append(arr.count(i))

print(lst.index((max(lst)))+1)

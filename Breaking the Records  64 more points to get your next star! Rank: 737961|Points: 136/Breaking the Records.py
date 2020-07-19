n=int(input())
scr=list(map(int,input().split()))
max_scr=scr[0]
min_scr=scr[0]
count_max=0
count_min=0

for i in scr:
    if (max_scr < i):
        max_scr=i
        count_max+=1

for j in scr:
    if (min_scr > j):
        min_scr=j
        count_min+=1
    else:
        continue
        
print(count_max,count_min)

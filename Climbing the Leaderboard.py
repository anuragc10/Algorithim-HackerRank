n=int(input())
score=list(map(int,input().split()))
m=int(input())
alice=list(map(int,input().split()))

set_score=set(score)

for i in alice:
    lst=list()
    p=set(set_score)
    p.add(i)
    lst=list(p)
    lst.sort(reverse=True)
    print(lst.index(i)+1)
    lst.clear()
    p.clear()
    
    

n=int(input())
shared=5
count=0

for day in range(1,n+1):
    liked=shared//2
    count=count+liked
    shared=liked*3
print(count)
        

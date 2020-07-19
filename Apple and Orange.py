s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
ora=0
app=0

apple=list(map(int,input().split()))
orange=list(map(int,input().split()))

for k in apple:
    if (a+k)>=s and (a+k)<=t:
        app=app+1
    else:
        continue

for p in orange:
    if (b+p)>=s and (b+p)<=t:
        ora=ora+1
    else:
        continue

print(app)
print(ora)

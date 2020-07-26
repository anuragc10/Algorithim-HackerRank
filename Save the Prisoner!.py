n=int(input())

for i in range(n):
    n,m,s=map(int,input().split())
    value=(n+m+s-1)%n
    if(value==0):
        print(n)
    else:
        print(value)
            

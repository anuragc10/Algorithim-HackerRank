
def solve(n,p):
    if(p<=n):
        return(min(p//2,n//2-p//2))

n=int(input())
p=int(input())
result=solve(n,p)
print(result)
    

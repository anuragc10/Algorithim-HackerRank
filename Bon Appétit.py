n,k=map(int,input().split())
bill=list(map(int,input().split()))
b=int(input())

bill.remove(bill[k])

p=sum(bill)/2

if(p==b):
    print("Bon Appetit")
else:
    print(int(b-p))


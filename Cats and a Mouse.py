n=int(input())

for i in range(n):
    A,B,C=map(int,input().split())
    if abs(C-A)==abs(B-C):
        print("Mouse C")
    elif abs(C-A)>abs(B-C):
        print("Cat B")
    else:
        print("Cat A")
        

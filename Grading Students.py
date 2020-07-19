n=int(input())
for i in range(n):
    k=int(input())
    if k>37:
        if (k+1)%5==0:
            print(k+1)
        elif (k+2)%5==0:
            print(k+2)
        else:
            print(k)
    else:
        print(k)

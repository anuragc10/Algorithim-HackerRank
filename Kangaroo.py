x1,v1,x2,v2=map(int,input().split())


if x1==x2 and v1==v1:
    print("YES")
elif x1==x2 and v1>v2:
    print("NO")
elif x1<=x2 and v1<=v2:
    print("NO")
else:
    if (x2-x1)%(v2-v1)==0:
        print("YES")
    else:
        print("NO")

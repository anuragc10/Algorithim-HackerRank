t=int(input())

for i in range(t):
    b,w=map(int,input().split())
    bc,wc,z=map(int,input().split())

    print(min(b*bc,b*(wc+z))+min(w*(bc+z),w*wc))

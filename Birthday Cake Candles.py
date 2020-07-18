N=int(input())
arr=list(map(int,input().split()))
arr.sort()
big=arr[len(arr)-1]
candle=0
for i in range(len(arr)):
    if(arr[i]==big):
        candle+=1
    else:
        continue
print(candle)

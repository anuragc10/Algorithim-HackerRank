words=input()

count=1
for i in range(len(words)):
    if(words[i].isupper()):
        count=count+1
print(count)

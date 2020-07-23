letter=list(map(int,input().split()))
word=input()
max_h=0

for i in range(len(word)):
    if(max_h<=letter[ord(word[i])-97]):
        max_h=letter[ord(word[i])-97]

print(max_h*len(word))


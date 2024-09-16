n=int(input())
words=[input() for i in range(n)]
words_occurences={}
for word in words:
    words_occurences[word]=0
for word in words:   
    words_occurences[word]+=1  
print(len(words_occurences))
occurences=words_occurences.values()
for i in occurences:
    print(i,end=" ")

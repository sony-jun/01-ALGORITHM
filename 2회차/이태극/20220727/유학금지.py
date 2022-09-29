chk="CAMBRIDGE"
word=list(input())
new_word=[]
for j in range(len(word)):
    for i in (chk):
        if i  in word:
            word.remove(i)
print("".join(word))
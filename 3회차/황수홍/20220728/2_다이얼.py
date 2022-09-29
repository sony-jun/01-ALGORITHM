dic = ['','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
cnt = 0

for i in range(len(word)):
    for j in dic :
        if word[i] in j:
            cnt += dic.index(j) + 1
print(cnt+len(word))
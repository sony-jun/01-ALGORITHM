from re import L


document = input()
word = input()
cnt = 0
for i in range(len(document)):
    if word in document:
        document = document.replace(word,'_',1)
        cnt+=1
    else:
        break
print(cnt)
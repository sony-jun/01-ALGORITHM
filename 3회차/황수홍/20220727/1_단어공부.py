words = input().upper()
word = list(set(words))

list = []

for i in word :
    cnt = words.count(i)
    list.append(cnt)

if list.count(max(list)) > 1 :
    print('?')
else :
    max = list.index(max(list))
    print(word[max])
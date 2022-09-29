word = input()
ban = 'CAMBRIDGE'

for i in word:
    if i in ban:
        word = word.replace(i,'')
print(word)
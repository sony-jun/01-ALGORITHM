cam = ['C','A','M','B','R','I','D','G','E']
word = input()

for i in word:
    if i in cam:
        word=word.replace(i,'')
print(word)
word = input()
word = word.lower()

alpha = 'abcdefghijklmnopqrstuvwxyz'
cntlist = []
for i in alpha:
    cntlist.append(word.count(i))

m = max(cntlist)
answer = []
for i, k in enumerate(cntlist):
    if k == m:
        answer.append(i)

if len(answer) == 1:
    print(alpha[answer[0]].upper())
else:
    print('?')
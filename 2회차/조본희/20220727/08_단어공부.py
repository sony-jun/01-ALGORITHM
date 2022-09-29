word = input()
word = word.lower()

#알파벳 문자열을 만들고 대조하며 cntlist에 각 알파벳의 갯수를 저장
alpha = 'abcdefghijklmnopqrstuvwxyz'
cntlist = []
for i in alpha:
    cntlist.append(word.count(i))

#max함수로 가장 많이 쓰인 알파벳을 answer에 저장
m = max(cntlist)
answer = []
for i, k in enumerate(cntlist):
    if k == m:
        answer.append(i)

#가장 많이쓰인 알파벳이 하나가 아닐 경우를 위한 조건문
if len(answer) == 1:
    print(alpha[answer[0]].upper())
else:
    print('?')
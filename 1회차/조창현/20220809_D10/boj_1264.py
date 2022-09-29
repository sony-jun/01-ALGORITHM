## 영문을 입력받아
## 모음의 개수를 센다. 'a, e, i, o, u' 대소문자 둘다
## 각 줄마다 영어 대소문자, ',', '.', '!', '?', 공백으로 이루어진 문장이 주어진다.
## 입력의 끝에는 한 줄에 '#' 한 글자만이 주어진다.

import sys
sys.stdin = open('1264.txt')

sentence = []

while True:
    sent = input()
    if sent == '#':
        break
    sentence.append(sent)
print(sentence)


for i in sentence:
    cnt = 0
    alpha = i[::1]
    if str(alpha) == 'a':
        print('a')
        cnt += 1
    print(cnt)
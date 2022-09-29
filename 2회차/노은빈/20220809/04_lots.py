import sys
sys.stdin = open('input.txt')

word = sys.stdin.read()
sen = [] #문장리스트
alpha = 'abcdefghijklmnopqrsyuvwxyz' 

for i in alpha :
    sen.append(word.count(i)) #alpha에 값이 있다면 i 값을 세기

max_ = max(sen)  #문장리스트에서 가장 많이 있는 알파벳 값 구하기
for i in range(len(word)):
    if max_ == word[i]: #가장 많이 있는 값과 i가 같다면
        print(chr(i+97), end = '') #chr(97) = a /공백 없이
    

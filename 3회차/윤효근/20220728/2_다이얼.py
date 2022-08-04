import sys


sys.stdin = open("2_다이얼.txt")


dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
#인덱스를 이용한 계산을 위해 리스트 작성

w=input()
result=0

for j in range(len(w)):
    for i in dial:      #리스트 안의 요소검사
        if w[j] in i:
            result += dial.index(i)+3
            #일치시 인덱스 +3초(숫자 1은 문자가 없고 2초부터 시작하며 1초씩 늘어나기 때문
            # 따라서 ABC = 인덱스 0이지만 2번 다이얼이고 3초가 걸림)
print(result)
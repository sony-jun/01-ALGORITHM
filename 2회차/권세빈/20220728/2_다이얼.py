# https://www.acmicpc.net/problem/5622

alpabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# 알파벳 담기

result = 0
word = input()

for i in word:                              # 입력값에서 하나 꺼냄 
    for j in alpabet:                       # 알파벳 리스트에서 하나 꺼냄
        if i in j:                          # 만약 입력값이 알파벳 리스트 안에 있다면 
            result += alpabet.index(j)+3    # 알파벳 리스트에서 인덱스 위치를 찾고
                                            # 숫자 1 거는데 2초 + 인덱스는 0부터 시작해서 1초
print(result)
                                            
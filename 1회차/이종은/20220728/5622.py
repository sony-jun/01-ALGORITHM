# 다이얼 


alpabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PORS', 'TUV', 'WXYZ']
word = input()

time = 0
for i in alpabet : 
    for n in i : # 알파벳 리스트에서 꺼낸 요소를 또 분리
        for x in word :  # 입력 받은 문자를 하나씩 분리 
            if n == x : 
                time += alpabet.index(i) + 3 # 다이얼 자리가 각 인덱스값에서 +3이기 때문에 

print(time)


# 딕셔너리 사용하는 코드 => 문제 쉽게 풀 수 있음


# 계산되어 출력될 초를 위해 alpha 생성, 문자열 입력
alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input()

# 문자열의 길이만큼 반복되는 for문
min_time = 0
for i in range(len(word)):
    # 문자열 앞부터 하나씩 alpha에 있는지 체크
    for j in alpha:
        # 만약 있을 경우 인덱스+3초 걸리므로 조건 설정
        if word[i] in j:
            min_time += alpha.index(j) + 3

print(min_time)

# 다이얼
# 문제 : 첫째 줄에 다이얼을 걸기 위해 필요한 최소 시간을 출력
# 접근 : 입력받은 문자를 리스트 안에서 찾고, 해당 인덱스 값으로 더해가기

number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alpha = list(input())

time = 0

for i in alpha:
    for j in number:
        if i in j:
            time += number.index(j) + 3  # 인덱스는 0부터, 알파벳은 3부터

print(time)

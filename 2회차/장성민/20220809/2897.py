# 행과 열의 개수 입력받기
R, C = map(int, input().split())
park = []
# 각 줄 리스트에 할당
for _ in range(R):
    li = list(input())
    park.append(li)
# 2행 2열의 칸 범위 돌면서 추가
monster = []
for i in range(R - 1):
    for j in range(C - 1):
        monster.append([park[i][j], park[i][j+1], park[i+1][j], park[i+1][j+1]])
# 결과를 위한 리스트 생성
result = [0 for _ in range(5)]
# 각 조건별로 공간의 개수 세기
for i in range(len(monster)):
    if '#' in monster[i]:
        continue
    elif monster[i].count('.') == 4:
        result[0] += 1
    elif monster[i].count('X') == 1:
        result[1] += 1
    elif monster[i].count('X') == 2:
        result[2] += 1
    elif monster[i].count('X') == 3:
        result[3] += 1
    elif monster[i].count('X') == 4:
        result[4] += 1
# 결과 출력
for i in range(len(result)):
    print(result[i])
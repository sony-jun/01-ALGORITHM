# 백준 5533
# 각 플레이어는 1 이상 100 이하의 정수를 카드에 적어 제출
# 각 플레이어는 자신과 같은 수를 쓴 사람이 없다면
# 자신이 쓴 수와 같은 점수를 얻는다
# 만약 같은 수를 쓴 다른 사람이 있는 경우 점수를 얻을 수 없다
# 이 게임을 3번 해서 각 플에이어가 각각 쓴 수가 주어졌을 때
# 3번 게임에서 얻은 총 점수를 구하는 프로그램

# 첫째 줄에 참가자의 수 N이 주어진다
# 둘째 줄부터 N개 줄에는 각 플레이어가
# 1번째, 2번째, 3번째 게임에서 쓴 수가 공백으로 구분되어 주어진다.

# 각 플레이어가 3번의 게임에서 얻은 총 점수를
# 입력으로 주어진 순서대로 출력

import sys
sys.stdin = open('유니크.txt', 'r')

N = int(input())
score = [[], [], []]
result = []

for _ in range(N):
    # 숫자1, 숫자2, 숫자3을 받아서 따로 리스트에 추가
    num1, num2, num3 = map(int, input().split())
    score[0].append(num1)
    score[1].append(num2)
    score[2].append(num3)

for i in range(N):
    s_score = 0
    for j in range(3):
        # 각 열의 값 중 입력한 값이 중복되지 않으면 그 값을 s_score에 더함
        if score[j].count(score[j][i]) == 1:
            s_score += score[j][i]
    # 더한 숫자들을 추가
    result.append(s_score)

# result에 있는 값을 하나씩 꺼내 출력
for number in result:
    print(number)
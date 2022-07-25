# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

# 테스트 케이스
t = int(input())

# 케이스만큼 반복
for i in range(1, t + 1):
    # 문자열 리스트 형태로 입력
    n = list(input())
    # 'O' 가 연속될 때마다 오르는 수
    cnt = 0
    # 총합
    result = 0

    # 리스트 안 문자열을 순차적으로 반복
    for j in n:
        # 'O' 라면
        if j == 'O':
            # 1을 추가하고 총합에 더하기
            cnt += 1
            result += cnt
        # 'O' 가 아니라면
        else:
            # 카운트 리셋
            cnt = 0

    print(result)

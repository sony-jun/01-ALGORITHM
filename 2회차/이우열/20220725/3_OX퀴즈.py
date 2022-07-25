# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

t = int(input())

for i in range(t):
    s = list(input())
    cnt = 0
    result = 0
    for j in s:
        if j == 'O':
            cnt += 1            # O일 때 점수를 1씩 증가시키고
            result += cnt       # 결과에 점수를 누적한다
        else:
            cnt = 0             # X일 때 점수를 초기화한다
    print(result)

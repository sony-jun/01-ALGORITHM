# https://www.acmicpc.net/problem/23253
# 아래 풀이로 시간초과 떴으니 다른 풀이 방법도 생각해보기

import sys
sys.stdin = open("23253_input.txt")

# 1번째 입력: 책 권수(N), 책 더미수(M)
N, M = map(int, input().split())

# 이 책들을 정리할 수 있나요?
OX = True

for i in range(M):

    # 2번째, 4번째, 6번째 ... 입력: 1번째, 2번째, 3번째 ... 더미에 포함된 책 권수
    int(input())

    # 1번째, 2번째, 3번째 ... 더미에 들어있는 책들의 번호 나열
    dummy = list(map(int, input().split()))

    # 만약에 dummy가 순서대로 sorted 되어 있지 않으면, OX = False 하고 연산 break
    if dummy != sorted(dummy, reverse = True):
        OX = False
        break

if OX: 
    print('Yes')
else:
    print('No')


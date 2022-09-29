#체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.

import sys
sys.stdin = open('킹퀸룩비숍나이트폰.txt') 

chess = list(map(int,input().split()))

basic = [1, 1, 2, 2, 2, 8]

answer = []

for a in range(len(basic)):
    c = basic[a] - chess[a]
    answer.append(c)

print(*answer)
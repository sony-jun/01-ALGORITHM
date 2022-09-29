# https://www.acmicpc.net/problem/1100

# 크기 8*8 흑칸 흰칸 번갈아가며 있음  (0,0)은 흰칸 
# .은 빈칸, F는 말 
# 요구사항 : 흰칸 위 말의 개수

from pprint import pprint
import sys
sys.stdin = open('72_하얀 칸.txt')

n = 8
m = 8
pan = [list(input()) for _ in range(n)]
# pprint(pan)
cnt = 0

for i in range(n):
    for j in range(m):
        if (i + j)%2 == 0:
        # 하얀칸은 (0,0)부터 검은칸과 번갈아가며 판을 만드므로 (i,j)의 값을 더하면 짝수인 경우가 된다
            if pan[i][j] == 'F':
            # 인덱스 합이 짝수인 하얀칸 중에 pan[i][j]의 값이 'F'로 말이 있다면 카운트
                cnt += 1

print(cnt)




# https://www.acmicpc.net/problem/1236
import sys
sys.stdin = open('0.txt', 'r')

n, m = map(int,input().split())
castle = [list(input()) for _ in range(n)]

n_cnt = 0 # 행 카운트
m_cnt = 0 # 열 카운트


# 행에 X가 없다면 행에 카운트 추가
for i in range(n):
    if 'X' not in castle[i]:
        n_cnt += 1

# 열을 기준으로 리스트로 묶어줌
for j in range(m):
    col = [castle[i][j] for i in range(n)]

    # 만약 열에 X가 없다면 열에 카운트 추가
    if 'X' not in col:
        m_cnt += 1
        
# 행과 열 중에 가장 큰 수 출력               
print(max(n_cnt,m_cnt))

        
        
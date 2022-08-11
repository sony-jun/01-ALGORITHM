# 순차적으로 돌면서 4개 범위 안에 문자로 판단
# #있으면 pass x가 0개, 1개, 2개, 3개, 4개 각각 카운트 업
from pprint import pprint


n, m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
answer = [0]*5
dx = [0,1,0,1]
dy = [0,0,1,1]
# pprint(matrix)
for y in range(m-1):
    for x in range(n-1):
        cnt = 0
        breaker = False
        for i in range(4):

            x_ = x + dx[i]
            y_ = y + dy[i]

            if matrix[x_][y_] == '#':

                breaker = True
                break
            elif matrix[x_][y_] == 'X':
                cnt += 1
        if breaker == True:
            continue
        answer[cnt] += 1
print(*answer, sep='\n')
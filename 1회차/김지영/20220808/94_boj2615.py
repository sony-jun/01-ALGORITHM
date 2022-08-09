# 오목
# not 6
# 승패결정
# n = 19
# 검 = 1 흰 = 0
# 델타리스트를 우,하,우하,우상으로 만들어야함
dy = [0,1,1,-1]
dx = [1,0,1,1]

n,m = map(int,input().split())
board = []
for _ in range(n):
    temp = list(map(int,input().split()))
    board.append(temp)

for y in range(n):
    for x in range(m):
        for d in range(4 ):
            ny = y + dy[d]
            nx = x + dx[d]

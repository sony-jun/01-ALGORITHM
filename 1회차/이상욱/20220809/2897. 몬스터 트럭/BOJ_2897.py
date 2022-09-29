import sys
sys.stdin = open('2897.txt')

R, C = map(int, input().split()) # 행과 열을 받아옴

case = [list(input()) for _ in range(R)] # input을 받아옴

dr = [0, 0, 1, 1] # 시계방향
dc = [0, 1, 1, 0] # 시계방향
x = 0
y = 0
monster = [0] * 6 # 부수고 주차할 공간의 개수


for r in range(R-2+1): 
    for c in range(C-2+1):
        car = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < R and 0 <= nc < C:
                x = nr
                y = nc
        
            if case[x][y] == '#':
                car = 5
                break
            elif case[x][y] == 'X':
                car += 1
        monster[car] += 1

for i in range(5):
    print(monster[i])

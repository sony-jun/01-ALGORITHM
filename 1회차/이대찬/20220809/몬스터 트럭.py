import sys

sys.stdin = open('몬스터 트럭.txt')

R,C = map(int,input().split())

matrix = [list(input()) for _ in range(R)]

델타_y = [0,0, 1, 1]
델타_x = [0,1, 1, 0]

result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

for y in range(R-1):
    for x in range(C-1):
        T=0
        cnt = 0
        for d in range(4):
            탐색_x = x + 델타_x[d]
            탐색_y = y + 델타_y[d]
            if matrix[탐색_y][탐색_x] == '#':
                T=1
                break
            if matrix[탐색_y][탐색_x] == 'X':
                cnt +=1
        if T == 0:
            result[cnt] +=1
                
for i in result:
    print(result[i])
 
 
n = int(input())
land_bomb = [list(input()) for i in range(n)]
status = [list(input()) for i in range(n)]
result = [list('.' for i in range(n)) for i in range(n)]

dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]

find_bomb = False

for y in range(n):
    for x in range(n):
        if status[y][x] == 'x':
            bomb=0
            for k in range(8):
                d_y = y+dy[k]
                d_x = x+dx[k]
                if  0 <= d_x < n  and  0 <= d_y < n :
                    if land_bomb[d_y][d_x] == '*':
                        bomb+=1
            result[y][x]=bomb
            if land_bomb[y][x] == '*':
                find_bomb = True

if find_bomb == True:
    for y in range(n):
        for x in range(n):
            if land_bomb[y][x] == '*':
                result[y][x] = '*'
for res in result:
    print(*res,sep='')



n = int(input())
bombs = [list(input()) for i in range(n)]
play = [list(input()) for i in range(n)]
result = [list('.' for i in range(n)) for i in range(n)]

dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]

find_b = False

for y in range(n):
    for x in range(n):
        if play[y][x] == 'x':
            bomb = 0
            for i in range(8):
                d_x = x+dx[i]
                d_y = y+dy[i]
                if 0 <= d_y < n and 0 <= d_x < n:
                    if bombs[d_y][d_x] == '*':
                        bomb+=1
            result[y][x] = bomb

            if bombs[y][x] == '*':
                find_b = True
if find_b == True:
    for y in range(n):
        for x in range(n):
            if bombs[y][x] == '*':
                result[y][x] = '*'
for res in result:
    print(*res,sep='')
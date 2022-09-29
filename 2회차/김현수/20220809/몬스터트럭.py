import sys
sys.stdin = open("몬스터트럭.txt")

from pprint import pprint

dx = [0,1,0,1] #탐색범위
dy = [0,0,1,1]
R, C = map(int,input().split()) # 행 열 입력

area = [list(input()) for _ in range(R)] #주차공간 입력
pprint(area)
print('---------')
result = [0]*5 #결과를 넣을 변수 [0,0,0,0,0]
for a in range(R-1): #0 ~ 2 3개씩
    for b in range(C-1): #0 ~ 2 3개씩
        monster = [area[a+dx[_]][b+dy[_]] for _ in range(4)] #트럭이 들어가는 위치에 있는 '.' '#' 'X'
        #print(monster, b)
        if '#' in monster:
            continue
        elif monster.count('.') == 4:
            result[0] += 1
        elif monster.count('X') == 1:
            result[1] += 1
        elif monster.count('X') == 2:
            result[2] += 1
        elif monster.count('X') == 3:
            result[3] += 1
        elif monster.count('X') == 4:
            result[4] += 1

for i in range(len(result)):
    print(result[i])

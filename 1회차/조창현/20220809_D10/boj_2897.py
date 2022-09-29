import sys
sys.stdin = open('2897.txt')

def pprint(in_list):
    for i in in_list:
        print(i)
    print('====================')

## 주차장의 x y 값
r, c = map(int, input().split())

## 주차장의 x y 값을 가지고 주차장 구현
parking_r = [list(map(str, input())) for _ in range(r)]
#pprint(parking_r)

## 탐색을 위한 델타값들 자신을 포함하여 3 방향을 탐색하겠다.
dx = [0, 1, 1]
dy = [1, 1, 0]
## 파괴하면 공간이 나는 자리
dest = 0
## 그냥 공간이 있는 자리
good = 0
## 주차를 할 수 없는 자리
cant = 0
## 인덱스 값만큼 파괴하면 주차를 할수 있을것
dest_list = [0] * 5

#######################################################################
############### 강사님 ################################################
#######################################################################

for r in range(r):
    for c in range(c):
        dest = 0
        if parking_r[r][c] == '#':
            ## 성립 못하는 조건은 무시
            continue
        elif parking_r[r][c] == 'X':
            dest += 1
        for d in range(3):
            next_r = r + dx[d]
            next_c = c + dy[d]
            if not(-1 < next_r < r and -1 < next_c < c):
                break
            if parking_r[next_r][next_c] == '#':
                break
            if parking_r[next_r][next_c] == 'X':
                dest += 1
        else:
            dest_list[dest] += 1

for i in dest_list:
    print(dest_list[i])



#######################################################################
############### 나 ################################################
#######################################################################

# for x in range(r):
#     for y in range(c):
#         dest = 0
#         good = 0
#         ## x y 에 +1 해도 주차장의 범위를 나가지 않도록
#         if x + 1 < r and y + 1 < c:
#             if parking_r[x][y] == '#':
#                 cant = 1
#                 #print('===== 기준 =======')
#                 #print(f'기준이 {x} {y}일 때 건물이 있어')
#             elif parking_r[x][y] == 'X':
#                 dest += 1
#                 #print('===== 기준 =======')
#                 #print(f'기준이 {x} {y}일 때 dest {dest}')
#                 for d in range(3):
#                     nx = x + dx[d]
#                     ny = y + dy[d]
#                     if parking_r[nx][ny] == '#':
#                         #print(f'{nx} {ny}일 때 건물이 있어')  
#                         cant = 1
#                     elif parking_r[nx][ny] == 'X':
#                         dest += 1
#                         #print(f'{nx} n{y}일 때 dest {dest}')
#                     elif parking_r[nx][ny] == '.':
#                         good += 1
#                         #print(f'{nx} {ny}일 때 good {good}')
#             elif parking_r[x][y] == '.':
#                 good += 1
#                 # print('===== 기준 =======')
#                 # print(f'기준이 {x} {y}일 때 good {good}')
#                 for d in range(3):
#                     nx = x + dx[d]
#                     ny = y + dy[d]
#                     if parking_r[nx][ny] == '#':
#                         #print(f'{nx} {ny}일 때 건물이 있어')  
#                         cant = 1
#                     elif parking_r[nx][ny] == 'X':
#                         dest += 1
#                         #print(f'{nx} {ny}일 때 dest {dest}')
#                     elif parking_r[nx][ny] == '.':
#                         good += 1
#                         #print(f'{nx} {ny}일 때 good {good}')
#         if good + dest == 4:
#             #print('wkfldy')
#             dest_list[dest] += 1
# for i in dest_list:
#     print(i)


# 1652
# 코레스코 콘도에 있는 방은 NxN의 정사각형 모양으로 생김
# 방 안에는 옮길 수 없는 짐들이 많이 있어 누울 자리를 차지하고 있음
# 누울 수 있는 자리에는 조건이 있다
# 똑바로 연속해서 2칸 이상의 빈 칸이 존재하면
# 그 곳에 몸을 양 옆으로 쭉 뻗으면서 누울 수 있다
# 가로로 누울 수도 있고 세로로 누울 수도 있다
# 누울 때는 무조건 몸을 쭉 뻗기 때문에 반드시 벽이다 짐에 닿게 됨

# 방의 크기 N과 방의 구조가 주어졌을 때
# 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수

# 첫째 줄에 방의 크기 N이 주어진다
# 그 다음 N줄에 걸져 N개의 문자가 들어오는데
# '.'은 아무것도 없는 곳을 의미하고
# 'X'는 짐이 있는 곳을 의미

import sys
sys.stdin = open('누울자리를찾아라.txt', 'r')

N = int(input())
room = []

for _ in range(N):
    #* room에 ['X'] 를 추가해서 '.' 개수를 초기화하고
    #* 마지막이 'X'가 아닐 때 '.'가 2개 이상이면
    #* 누울 수 있는 자리에 추가함
    room.append(list(map(str, input())) + ['X'])
room.append(['X' for _ in range(N + 1)])

res = [0, 0]

for i in range(N + 1):
    cnt_h, cnt_v = 0, 0
    for j in range(N + 1):
        if room[i][j] == '.':
            cnt_h += 1
        elif room[i][j] == 'X':
            if cnt_h >= 2:
                res[0] += 1
            cnt_h = 0
        
        if room[j][i] == '.':
            cnt_v += 1
        elif room [j][i] == 'X':
            if cnt_v >= 2:
                res[1] += 1
            cnt_v = 0

print(' '.join(map(str, res)))
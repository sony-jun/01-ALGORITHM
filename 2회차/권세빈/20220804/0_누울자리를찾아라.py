# https://www.acmicpc.net/problem/1652

import sys
sys.stdin = open('0.txt', 'r')
from pprint import pprint
# input = sys.stdin.readline

n = int(input())
# 가로방
w_room = [list(input()) for _ in range(n)]
# 세로방
h_room = [[0] * n for _ in range(n)]

w_cnt = 0   # 가로 누울 자리 개수
h_cnt = 0   # 세로 누울 자리 개수

# 세로방 만들기 및 빈공간 찾기 위한 이중 반복문
for i in range(n):  
    w_space = 0 # 가로 빈공간
    h_space = 0 # 세로 빈공간

    for j in range(n):
        # 가로방의 행열을 반대로 해서 세로방 만들기
        h_room[i][j] = w_room[j][i]

        # 만약 가로방에 '.'이 있다면 빈공간 추가
        if w_room[i][j] == '.':
            w_space += 1

        # 바로 다음 '.'이 없다면 빈공간 0으로 초기화
        else:
            w_space = 0

        # 만약 빈공간이 2라면 누울자리 1씩 추가
        # w_space >= 2 이렇게 하면 누울자리 중복돼서 안됨
        if w_space == 2:
            w_cnt += 1

        # 가로방과 똑같이 세로방도 진행
        if h_room[i][j] == '.':
            h_space += 1
        else:
            h_space = 0

        if h_space == 2:
            h_cnt += 1

print(w_cnt, h_cnt)


# for w in w_room:
#     for k in range(n-1):
#         if w[k] == '.' and w[k+1] == '.':
#             w_cnt += 1
#             break

# for h in h_room:
#     for l in range(n-1):
#         if h[l] == '.' and h[l+1] == '.':
#             h_cnt += 1
#             break

# print(w_cnt,h_cnt)


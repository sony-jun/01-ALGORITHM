# https://www.acmicpc.net/problem/2615

import sys
sys.stdin = open("input.txt")

go_board = [list(map(int, input().split())) for _ in range(19)]
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        now = go_board[x][y]


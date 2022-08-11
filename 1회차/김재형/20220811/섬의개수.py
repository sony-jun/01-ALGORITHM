import sys
sys.stdin = open('섬의개수_input.txt')

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


while True:
    w, h = map(int, input().split())
    island = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            
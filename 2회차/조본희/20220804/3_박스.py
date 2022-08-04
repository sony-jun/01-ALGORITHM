import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for i in range(m)]
    box = list(map(list, zip(*box)))
    cnt = 0

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                cnt += box[i][j+1:].count(0)
    print(cnt)
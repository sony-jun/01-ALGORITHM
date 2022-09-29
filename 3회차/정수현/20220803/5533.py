import sys
sys.stdin = open('5533.txt')

N = int(sys.stdin.readline())
scores = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
total = [0] * N
for j in range(3):
    for i in range(N):
        if [scores[i][j] for i in range(N)].count(scores[i][j]) == 1:
            total[i] += scores[i][j]
for i in range(N):
    print(total[i])
        
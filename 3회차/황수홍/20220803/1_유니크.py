from sys import stdin

N = int(stdin.readline())
score = [[],[],[]]

for _ in range(N):
    a, b, c = map(int,stdin.readline().split())
    score[0].append(a)
    score[1].append(b)
    score[2].append(c)

for i in range(N):
    s = 0
    for j in range(3):
        if score[j].count(score[j][i]) == 1:
            s += score[j][i]
    print(s)
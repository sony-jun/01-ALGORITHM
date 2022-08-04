# https://www.acmicpc.net/problem/5533

N = int(input()) #참가자 수
scores = []

for i in range(N):
    scores.append(list(map(int, input().split())))

s = 0
sum_ = []
for i in range(N):
    for j in range(3):
        if scores[j].count(scores[j][i]) == 1:
            s += scores[j][i]
    sum_.append(s)
for i in sum_:
    print(i)
        

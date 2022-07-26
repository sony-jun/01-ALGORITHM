# https://www.acmicpc.net/problem/2846

T = int(input())
P = list(map(int, input().split()))
P += [0]
start = P[0]
result = 0

for i in range(1, T+1):
    if P[i] > P[i-1]:
        continue
    else:
        if result > P[i - 1] - start:
            start = P[i]
            continue
        else :
            result = P[i - 1] - start
        start = P[i]

print(result)
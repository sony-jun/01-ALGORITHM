import sys

sys.stdin = open("90.블랙잭.txt")

N, M = list(map(int, input().split()))

cards = list(map(int, input().split()))
max_total = 0
# 완전탐색(Brute-force)
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            total  = cards[i] + cards[j] +cards[k]

            if total > M:
                continue
            else:
                max_total = max(max_total, total)

print(max_total)

            
                

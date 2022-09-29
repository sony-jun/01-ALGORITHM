import sys
sys.stdin = open("20220808/2798_블랙잭.txt")

N, M = map(int, input().split())
num = list(map(int, input().split()))
card = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            three = num[i] + num[j] + num[k]
            if three > M:
                continue
            else:
                card.append(three)

print(max(card))
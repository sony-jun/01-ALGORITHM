import sys
sys.stdin = open("0_블랙잭.txt", 'r')

N, M = map(int, sys.stdin.readline().split())
cards = [*map(int, sys.stdin.readline().split())]
max_ = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if cards[i] + cards[j] + cards[k] <= M and cards[i] + cards[j] + cards[k] > max_:
                max_ = cards[i] + cards[j] + cards[k]
            if max_ == M:
                break

print(max_)
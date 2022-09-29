import sys
sys.stdin = open('B2798.txt')

N, M = map(int, input().split())
cards = list(map(int, input().split()))
# print(N, M, cards)
total = []
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum_ = cards[i] + cards[j] + cards[k]
            if sum_ <= M:
                total.append(sum_)
print(max(total))
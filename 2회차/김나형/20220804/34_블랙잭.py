import sys
sys. stdin = open("34_블랙잭.txt")

N, M = map(int, input().split())
card = list(map(int, input().split()))
max_num = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if card[i] + card[j] + card[k] <= M:
                 num = card[i] + card[j] + card[k]
                 max_num = max(num, max_num)
           
print(max_num)
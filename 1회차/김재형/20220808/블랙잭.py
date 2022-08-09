import sys
sys.stdin = open('블랙잭_input.txt')

N, M = map(int, input().split())
# 5 21

card = list(map(int, input().split()))
total = 0

for x in range(N-2):
    for y in range(x + 1,N-1):
        for z in range(y+1,N):
            sum_ = 0
            sum_ = card[x] + card[y] + card[z]
            if sum_ <= M and sum_ > total:
                total = sum_
            
print(total)
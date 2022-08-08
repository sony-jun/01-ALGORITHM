# https://www.acmicpc.net/problem/2798

N, M = map(int, input().split())
card_nums = list(map(int, input().split()))
result = 0

for i in range(0,  N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = card_nums[i] + card_nums[j] + card_nums[k]
            if result <= temp and temp <= M:
                result = temp
print(result)
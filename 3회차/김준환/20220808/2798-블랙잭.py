import sys
input = sys.stdin.readline

n, m = map(int,input().split())
card_lst = list(map(int,input().split()))
card_sum = 0
max_sum = 0
breaker = False
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            card_sum = card_lst[i] + card_lst[j] + card_lst[k]
            if max_sum < card_sum <= m:
                max_sum = card_sum
            if card_sum == m:
                breaker = True
                break
        if breaker == True:
            break
    if breaker == True:
        break
print(max_sum)
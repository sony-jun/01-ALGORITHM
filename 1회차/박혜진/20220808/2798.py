# n장의 카드 중 3장을 고른다
# 3장의 카드 합은 m을 넘지 않으면서 가장 가까운 수

n, m = map(int, input().split())

cards = list(map(int, input().split()))
max_sum = 0

for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            sum = cards[i] + cards[j] + cards[k]

            if max_sum < sum <= m :
                max_sum = sum
            
            if sum == m :
                max_sum = sum

print(max_sum)
import sys
sys.stdin = open('2798.txt')
# n 카드 개수
# m 합의 근접값
n, m = map(int, input().split())
cards = list(map(str, input().split()))
#print(cards)

cards_sum = 0
cs_max = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            cards_sum = int(cards[i]) + int(cards[j]) + int(cards[k])
            if cards_sum == m:
                cs_max = cards_sum
            elif cards_sum < m and cards_sum > cs_max:
                cs_max = cards_sum
print(cs_max)
#print(cards_sum)

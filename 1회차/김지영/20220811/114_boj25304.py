# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액
import sys
sys.stdin = open('114_input.txt')

X = int(input()) # 총 금액
N = int(input()) # 구매한 물건의 종류의 수
total = 0
for _ in range(N):
    a,b = map(int,input().split()) # a = 물건의 가격, b = 물건의 개수
    total += a*b
print('Yes' if total == X else 'No')
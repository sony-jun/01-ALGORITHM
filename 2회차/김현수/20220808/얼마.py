import sys
sys.stdin = open("얼마.txt")

T = int(input())

for _ in range(T):
    price_sum = 0
    s = int(input()) #자동차 가격
    price_sum += s
    n = int(input()) #옵션개수
    if n > 0:
        for i in range(n):
            q, p =map(int,input().split())
            price_sum += q * p
    print(price_sum)
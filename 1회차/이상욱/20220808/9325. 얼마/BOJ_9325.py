import sys
sys.stdin = open('9325.txt')

T = int(input())
for t in range(1, T+1):
    S = int(input())
    n = int(input())
    sum = 0

    for i in range(n):
        q, p = map(int, input().split())
        sum += q * p

    print(S + sum)
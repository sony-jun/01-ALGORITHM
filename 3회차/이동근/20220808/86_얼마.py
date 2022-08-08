import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = int(input())

    n = int(input())
    opt = 0
    for i in range(n):
        q, p = map(int, input().split())
        opt += q * p

    print(s + opt)
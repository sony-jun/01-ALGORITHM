import sys

input = sys.stdin.readline

for test_case in range(1, int(input()) + 1):
    s = int(input())
    for _ in range(int(input())):
        q, p = map(int, input().split())
        s += q * p
    print(s)